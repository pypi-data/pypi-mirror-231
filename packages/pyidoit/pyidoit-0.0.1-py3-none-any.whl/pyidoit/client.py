import requests
import random
from typing import Union, List, Literal
from pyidoit.utils import CategoryField, DeleteStatusField, ObjectStatusField

class IDoitClient(object):
    """Simple i-doit python client.

    Args:
        object (_type_): _description_
    """
    def __init__(
        self,
        host: str,
        apikey: str,
        username: str,
        password: str,
        language: str = "en"
    ) -> None:
        self.url = host
        self.apikey = apikey
        self.username = username
        self.password = password
        self.language = language
        self.headers = {
            "Content-Type":"application/json",
            "Accept": "application/json"
        }
    
    def _execute_request(self, body, headers=None):
        if not headers: # if header is not provided use the default one
            headers = self.headers
        try:
            data = requests.post(
                self.url,
                json=body,
                headers=headers,
                auth=(self.username, self.password)
            )
        except:
            data = None

        return data.json()
        
    # idoit methods
    def idoit_search(self, q):
        """Search objects in i-doit.

        Args:
            q (str): The query for the search."""
        body = {
            "jsonrpc": "2.0",
            "method" :"idoit.search",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "q": q
            },
            "id": random.randint(1, 200)
        }
        
        data = self._execute_request(body)
        return data

    def idoit_version(self):
        """Fetch information about i-doit and the current user."""
        body = {
            "jsonrpc": "2.0",
            "method" :"idoit.version",
            "params": {
                "apikey": self.apikey,
                "language": self.language
            },
            "id": random.randint(1, 200)
        }
        data = self._execute_request(body)
        return data

    def idoit_constants(self):
        """Fetch all defined constants from i-doit."""
        body = {
            "jsonrpc": "2.0",
            "method" :"idoit.constants",
            "params": {
                "apikey": self.apikey,
                "language": self.language
            },
            "id": random.randint(1, 200)
        }
        data = self._execute_request(body)
        return data

    def idoit_login(self, username: str, password: str):
        """Create new session

        Args:
            username (str): the username.
            password (str): The password.
        """
        new_header = {**self.headers}
        new_header["X-RPC-Auth-Username"] = username
        new_header["X-RPC-Auth-Password"] = password
        body = {
            "jsonrpc": "2.0",
            "method" :"idoit.login",
            "params": {
                "apikey": self.apikey,
                "language": self.language
            },
            "id": random.randint(1, 200)
        }
        data = self._execute_request(body, headers=new_header)
        return data

    def idoit_logout(self, token: str):
        """Close current session

        Args:
            token (str): The session's token.
        """
        new_header = {**self.headers}
        new_header["X-RPC-Auth-Session"] = token
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.read",
            "params": {
                "apikey": self.apikey,
                "language": self.language
            },
            "id": random.randint(1, 200)
        }
        data = self._execute_request(body, headers=new_header)
        return data

    # cmdb objects methods
    def cmdb_object_create(
        self,
        type: Union[str, int],
        title: int,
        category: Union[CategoryField, None] = None,
        purpose: Union[str, None] = None,
        cmdb_status: Union[Union[str, int], None] = None,
        description: Union[str, None] = None
    ):
        """Create new object with some optional information

        Args:
            type (str | int): The object type constant as string or integer.
            title (str): The object title.
            category (CategoryField): The Category of the object.
            purpose (str): The purpose of the obejct.
            cmdb_status (str | int)	The cmdb status of the object as integer or string.
            description (str): The description of the object.
        """
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.read",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "type": type,
                "title": title
            },
            "id": random.randint(1, 200)
        }
        
        if category:
            body["params"]["category"] = category
        if purpose:
            body["params"]["purpose"] = purpose
        if cmdb_status:
            body["params"]["cmdb_status"] = cmdb_status
        if description:
            body["params"]["description"] = description

        data = self._execute_request(body)
        return data

    def cmdb_object_read(self, object_id: int):
        """Get a specific object.

        Args:
            object_id (int): The object identifier."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.read",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_update(self, object_id: int, title: str):
        """Update the title of a given object.

        Args:
            object_id (int): The object identifier.
            title (str): The new object title
        """
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.update",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id,
                "title": title
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_delete(
        self,
        object_id: int,
        status: DeleteStatusField
    ):
        """Delete a specific object or change it's status.

        Args:
            object_id (int): The object identifier.
            status (DeleteStatusField): The status that indicate the action to take.
        """
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.delete",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id,
                "status": status
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_recycle(self, object_id: int):
        """Recycle a speficic object.

        Args:
            object_id (int): The id of the object."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.recycle",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_archive(self, object_id: int):
        """Archibe a specific object.

        Args:
            object_id (int): The object identifier."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.Integer",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_purge(self, object_id: int):
        """Purge a specific object from the database.

        Args:
            object_id (int): The object identifier."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.purge",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_mark_as_template(self, object_id: int):
        """Set the Object condition as a Template.

        Args:
            object_id (int): The object identifier."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.markAsTemplate",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_object_mark_as_mass_change_template(self, object_id: int):
        """Set the Object condition as a Mass Change Template.

        Args:
            object_id (int): The object identifier."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.markAsMassChangeTemplate",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "id": object_id
            },
            "id": random.randint(1, 200)
        }

        data = self._execute_request(body)
        return data

    def cmdb_objects_read(
        self,
        limit: Union[int, None] = None,
        categories: Union[List[str], None] = None,
        order_by: Union[str, None] = None,
        sort: Union[Literal["ASC", "DESC"], None] = "ASC",
        ids: Union[List[int], None] = None,
        type: Union[int, str, None] = None,
        title: Union[str, None] = None,
        type_title: Union[str, None] = None,
        sysid: Union[str, None] = None,
        first_name: Union[str, None] = None,
        last_name: Union[str, None] = None,
        email: Union[str, None] = None,
        type_group: Union[str, None] = None,
        status: Union[ObjectStatusField, None] = None
    ):
        """Get the list of all available objects.

        Args:
            limit (int | int): Maximum amount of objects Combine this limit with an offset (as string),
                               for example, fetch the next thousand of objects: "1000,1000".
            categories (List[str]): The list of categories to filter on.
            order_by (str): Order result set by.
            sort (str): Only useful in combination with key order_by; allowed values are either
                        "ASC" (ascending) or "DESC" (descending).
            ids: (List[int]): List of object identifiers to filter on.
            type (int | str): Object type identifier to filter on.
            title (str): Object title (see attribute Title in category Global).
            type_title (str): Translated name of object type, for example: 'Server'.
            sysid (str): System's id (see category Global), for example: "SRV_101010".
            first_name (str): First name of an object of type Persons.
            last_name (str): Last name of an object of type Persons.
            email (str): e-mail address of an object of type Persons, Person groups or Organization.
            type_group (str): Filters by the object type group e.g. Infrastructure or Other.
            status (ObjectStatusField): Filter by status of the objects e.g. Normal or Archived.
        """
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.objects.read",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "filter": {}
            },
            "id": random.randint(1, 200)
        }

        if limit:
            body["params"]["limit"] = limit
        if categories:
            body["params"]["categories"] = categories
        if order_by:
            body["params"]["order_by"] = order_by
        if sort:
            body["params"]["sort"] = sort
        if ids:
            body["params"]["filter"]["ids"] = ids
        if type:
            body["params"]["filter"]["type"] = type
        if title:
            body["params"]["filter"]["title"] = title
        if type_title:
            body["params"]["filter"]["type_title"] = type_title
        if sysid:
            body["params"]["filter"]["sysid"] = sysid
        if first_name:
            body["params"]["filter"]["first_name"] = first_name
        if last_name:
            body["params"]["filter"]["last_name"] = last_name
        if email:
            body["params"]["filter"]["email"] = email
        if type_group:
            body["params"]["filter"]["type_group"] = type_group
        if status:
            body["params"]["filter"]["status"] = status

        data = self._execute_request(body)
        # print(data)
        return data

    # cmdb category methods

    def cmdb_category_save(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_create(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_update(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_delete(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_quickpurge(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_purge(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_recycle(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_archive(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    # cmdb dialog methods

    def cmdb_dialog_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_create(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_update(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_delete(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    # cmdb reports methods
    def cmdb_reports_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass
