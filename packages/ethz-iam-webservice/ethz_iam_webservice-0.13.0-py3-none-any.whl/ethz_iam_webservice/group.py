import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum

from .conn import IAMApi, IAMApiAlternative
from .verbose import VERBOSE


class RecertificationPeriod(Enum):
    ANNUAL = "Annual"
    QUARTERLY = "Quarterly"
    BIENNIAL = "Biennial"
    NONE = "No recertification"
    INVALID = "Not set or invalid value"


class GroupType(Enum):
    CUSTOM = "custom"
    LZ = "lz"
    GROUPS = "groups"
    DOMAIN = "domain"
    PERSKAT = "perskat"
    PRIVATE = "private"
    REALM = "realm"
    BUILDING = "building"


class Targets(Enum):
    AD = "AD"
    LDAP = "LDAP"


@dataclass
class GroupAlternative(IAMApiAlternative):
    cn: str = None
    description: str = None
    type: GroupType = None
    members: list[str] = None
    gidNumber: int = None

    def new_from_data(self, data):
        return GroupAlternative(
            cn=data.get("cn", ""),
            description=data.get("description", ""),
            type=data.get("type", ""),
            members=data.get("members", []),
            gidNumber=data.get("gidNumber", ""),
        )

    def search_groups(
        self,
        group_name,
        member,
        gidnumber,
        group_type,
        email,
        firstname,
        lastname,
        member_details: bool = False,
        no_members: bool = False,
    ):
        endpoint = "/groupmgr/groups?"
        query = {}
        if group_name:
            query["cn"] = group_name
        if member:
            query["member"] = member
        if gidnumber:
            query["gidNumber"] = gidnumber
        if group_type:
            query["type"] = group_type
        if email:
            query["mail"] = email
        if firstname:
            query["firstname"] = firstname
        if lastname:
            query["lastname"] = lastname
        if member_details:
            query["member_details"] = "true"
        if no_members:
            query["no_members"] = "true"

        querystring = "&".join(f"{k}={v}" for k, v in query.items())
        full_endpoint = endpoint + querystring
        data = self.get_request(full_endpoint)
        groups = []
        for d in data:
            groups.append(self.new_from_data(d))
        return groups


@dataclass
class Group(IAMApi):
    name: str = None
    description: str = None
    admingroup: str = None
    group_ad_ou: str = None
    cre_date: str = None
    mod_date: str = None
    grid: int = None
    gidNumber: int = None
    category: str = None
    state: str = None
    certification_date: str = ""
    certification_period: str = RecertificationPeriod.NONE.value
    certification_note: str = ""
    members: list[str] = field(default_factory=list)
    managers: list[str] = field(default_factory=list)
    targets: list[Targets] = field(default_factory=list)

    def new_from_data(self, data):
        new_group = {}
        new_group["certification_date"] = (
            datetime.strptime(data.get("certificationDate"), "%d.%m.%Y").isoformat(
                timespec="seconds"
            )
            if data.get("certificationDate")
            else ""
        )
        new_group["cre_date"] = datetime.fromisoformat(
            data["createTimestamp"][:-1]
        ).isoformat(timespec="seconds")
        new_group["mod_date"] = datetime.fromisoformat(
            data["modifyTimestamp"][:-1]
        ).isoformat(timespec="seconds")
        new_group["name"] = data["groupName"]
        new_group["category"] = data["groupRoleCategory"]
        new_group["admingroup"] = data["respAdminGroup"]
        new_group["members"] = data.get("users", [])
        new_group["members"] += data.get("subgroups", [])
        new_group["managers"] = data.get("groupManager", [])
        new_group["targets"] = []
        for target in data.get("targetSystems", []):
            new_group["targets"].append(
                "AD" if target == "Active Directory" else "LDAP"
            )

        new_group["group_ad_ou"] = data.get("groupADOU")
        new_group["certification_period"] = data.get("certificationPeriod")
        new_group["certification_note"] = data.get("certificationNote")

        for key in (
            "description",
            "grid",
            "gidNumber",
            "state",
        ):
            new_group[key] = data.get(key, "")
        group = Group(**new_group)
        group._admin_username = self._admin_username
        group._admin_password = self._admin_password
        return group

    def create(
        self,
        name: str,
        admingroup: str,
        description: str,
        targets: list[Targets] = None,
        group_ad_ou: str = None,
        certification_period: RecertificationPeriod = RecertificationPeriod.NONE.value,
        certification_note: str = None,
        managers: list[str] = None,
    ):
        map_targets = {
            "AD": "Active Directory",
            "ACTIVE DIRECTORY": "Active Directory",
            "LDAP": "LDAPS",
            "LDAPS": "LDAPS",
        }
        body = {
            "name": name,
            "description": description,
            "admingroup": admingroup,
            "targets": [map_targets[target.upper()] for target in targets],
            "groupADOU": group_ad_ou,
            "certificationPeriod": certification_period,
            "certificationNote": certification_note or "no recertification needed"
            if certification_period == RecertificationPeriod.NONE.value
            else "",
            "groupManager": managers,
        }

        endpoint = "/groups"
        data = self.post_request(endpoint, body)
        if VERBOSE:
            print("new group {} was successfully created".format(name))
        new_group = self.new_from_data(data)
        new_group._admin_username = self._admin_username
        new_group._admin_password = self._admin_password
        return new_group

    def update(
        self,
        current_name: str,
        new_name: str = None,
        description: str = None,
        group_ad_ou: str = None,
        certification_period: RecertificationPeriod = None,
        certification_note: str = None,
        managers: list[str] = None,
    ):
        payload = {}
        if new_name and new_name != self.name:
            payload["newName"] = new_name
        if description:
            payload["newDescription"] = description
        if managers:
            payload["newGroupManager"] = managers
        if group_ad_ou:
            payload["newGroupADOU"] = group_ad_ou
        if certification_period:
            payload["newCertPeriod"] = certification_period
            if certification_period == RecertificationPeriod.NONE.value:
                payload["newCertNote"] = (
                    certification_note or "no recertification needed"
                )
        if certification_note:
            payload["newCertNote"] = certification_note
            payload["newCertPeriod"] = RecertificationPeriod.NONE.value
        if not payload:
            return self

        endpoint = f"/groups/{current_name}"
        data = self.put_request(endpoint, payload)
        if VERBOSE:
            print(f"group {current_name} has been successfully updated")
        group = self.new_from_data(data)
        group._admin_username = self._admin_username
        group._admin_password = self._admin_password
        return group

    def replace_field_values(self, new_obj):
        for key in new_obj.data.keys():
            setattr(self, key, getattr(new_obj, key))

    @property
    def data(self):
        return asdict(self)

    def get_group(self, identifier=None):
        """Get a group by its group name or by gidNumber"""
        if re.search(r"^\d+$", str(identifier)):
            # we search using a gidNumber
            endpoint = f"/groups?gidNumber={identifier}"
            data = self.get_request(endpoint=endpoint)
            if len(data) == 1:
                data = data[0]
            elif len(data) > 1:
                raise ValueError(
                    f"More than one group found with gidNumber={identifier}"
                )
            else:
                raise ValueError(f"No group found with gidNumber={identifier}")
        else:
            endpoint = f"/groups/{identifier}"
            data = self.get_request(endpoint=endpoint)
        group = self.new_from_data(data)
        return group

    def add_members(self, users, subgroups):
        """Add members to a group: users and/or subgroups"""
        endpoint = f"/groups/{self.name}/members/add"
        payload = {"users": users, "subgroups": subgroups}
        data = self.put_request(endpoint, payload)
        group = self.new_from_data(data)
        self.replace_field_values(group)

    def remove_members(self, users, subgroups):
        """Remove the members of a group: users and/or subgroups"""
        endpoint = f"/groups/{self.name}/members/remove"
        payload = {"users": users, "subgroups": subgroups}
        data = self.put_request(endpoint, payload)
        group = self.new_from_data(data)
        self.replace_field_values(group)

    def set_members(self, users, subgroups):
        """Set the members of a group, replace all the previous ones."""
        endpoint = f"/groups/{self.name}/members"
        payload = {"users": users, "subgroups": subgroups}
        data = self.post_request(endpoint, payload)
        group = self.new_from_data(data)
        self.replace_field_values(group)

    def set_targets(self, targets):
        """Put the group in AD and/or LDAP"""
        map_targets = {
            "AD": "AD",
            "ACTIVE DIRECTORY": "AD",
            "LDAP": "LDAP",
            "LDAPS": "LDAP",
        }
        targets = [map_targets[target.upper()] for target in targets]
        if "AD" in targets and "LDAP" in targets:
            target_string = "ALL"
        else:
            target_string = targets[0].upper()
        endpoint = f"/groups/{self.name}/targetsystems/{target_string}"
        self.put_request(endpoint, {})
        if target_string == "ALL":
            self.targets = ["AD", "LDAP"]
        else:
            self.targets.append(target_string)

    def remove_targets(self, targets):
        """Remove the group from AD and/or LDAP."""
        map_targets = {
            "AD": "AD",
            "ACTIVE DIRECTORY": "AD",
            "LDAP": "LDAP",
            "LDAPS": "LDAP",
        }
        for target in [map_targets[target.upper()] for target in targets]:
            endpoint = f"/groups/{self.name}/targetsystems/{target.upper()}"
            resp = self.delete_request(endpoint)
            if resp.ok:
                self.targets = [t for t in self.targets if t != target]

    def delete(self):
        """Delete a group and remove it from all its target systems."""
        endpoint = f"/groups/{self.name}"
        resp = self.delete_request(endpoint)
        if resp.ok:
            if VERBOSE:
                print(f"group {self.name} was successfully deleted")
        elif resp.status_code == 401:
            raise ValueError(
                "Provided admin-username/password is incorrect or you are not allowed to do this operation"
            )
        else:
            data = resp.json()
            raise ValueError(data["msg"])

    def recertify(self):
        """Recertify and adjust the end date of a group"""
        endpoint = f"/groups/{self.name}/recertify"
        data = self.put_request(endpoint, "")
        group = self.new_from_data(data)
        self.replace_field_values(group)
        if VERBOSE:
            print(f"group {self.name} was successfully recertified")
