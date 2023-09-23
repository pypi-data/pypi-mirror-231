import json
import requests
from ploomes_client.core.ploomes_client import PloomesClient
from ploomes_client.core.utils import get_file_url


class Users:
    def __init__(self, client: PloomesClient) -> None:
        self.client = client
        self.path = "/Users"

    def get_users(
        self,
        filter_=None,
        expand=None,
        top=None,
        inlinecount=None,
        orderby=None,
        select=None,
        skip=None,
    ):
        """
        Retrieves users based on the provided filters.

        Args:
            filter_ (str, optional): OData filter string.
            expand (str, optional): Expand related entities.
            top (int, optional): Maximum number of results to return.
            inlinecount (str, optional): Option for inline count.
            orderby (str, optional): Order by clause.
            select (str, optional): Select specific properties.
            skip (int, optional): Number of results to skip.

        Returns:
            Response: The response object containing the result of the GET request.
        """
        filters = {
            "$filter": filter_,
            "$inlinecount": inlinecount,
            "$orderby": orderby,
            "$select": select,
            "$skip": skip,
            "$top": top,
            "$expand": expand,
        }
        return self.client.request(
            "GET",
            self.path,
            filters={k: v for k, v in filters.items() if v is not None},
        )

    def post_user(
        self,
        payload,
        filter_=None,
        expand=None,
        top=None,
        inlinecount=None,
        orderby=None,
        select=None,
        skip=None,
    ):
        filters = {
            "$filter": filter_,
            "$inlinecount": inlinecount,
            "$orderby": orderby,
            "$select": select,
            "$skip": skip,
            "$top": top,
            "$expand": expand,
        }
        payload_json = json.dumps(payload)
        return self.client.request(
            "POST",
            self.path,
            filters={k: v for k, v in filters.items() if v is not None},
            payload=payload_json,
        )

    def patch_user(
        self,
        id_: int,
        payload: dict,
        filter_=None,
        expand=None,
        top=None,
        inlinecount=None,
        orderby=None,
        select=None,
        skip=None,
    ):
        """
        Updates a user by its ID with specific fields.

        Args:
            id_ (int): The ID of the user to be updated.
            payload (dict): Fields to be updated in the user.
            filter_ (str, optional): OData filter string.
            inlinecount (str, optional): Option for inline count.
            orderby (str, optional): Order by clause.
            select (str, optional): Select specific properties.
            skip (int, optional): Number of results to skip.
            top (int, optional): Maximum number of results to return.
            expand (str, optional): Expand related entities.

        Returns:
            dict: The JSON response from the server.
        """
        filters = {
            "$filter": filter_,
            "$inlinecount": inlinecount,
            "$orderby": orderby,
            "$select": select,
            "$skip": skip,
            "$top": top,
            "$expand": expand,
        }
        payload_json = json.dumps(payload)
        return self.client.request(
            "PATCH",
            self.path + f"({id_})",
            filters={k: v for k, v in filters.items() if v is not None},
            payload=payload_json,
        )

    def delete_user(self, id_: int):
        """
        Deletes a user by its ID.

        Args:
            id_ (int): The ID of the user to be deleted.

        Returns:
            dict: The JSON response from the server.
        """
        return self.client.request("DELETE", self.path + f"({id_})")

    def post_user_avatar(self, user_id: int, image_url: str) -> dict:
        """
        Uploads an avatar for a specific user.

        Args:
            user_id (int): The ID of the user.
            image_url (str): The URL of the image to be used as the avatar.

        Returns:
            dict: The JSON response from the server containing the details of the uploaded avatar.
        """
        filename = get_file_url(image_url)  # Extract the filename from the URL
        files = [("file1", (filename, requests.get(image_url).content, "image/jpeg"))]
        headers = {"User-Key": self.client.api_key}

        return self.client.request(
            "POST",
            self.path + f"({user_id})/UploadAvatar",
            files=files,
            headers=headers,
        )