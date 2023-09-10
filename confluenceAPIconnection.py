from database import DatabaseConnection
import requests
import json
import base64

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the variables
label = os.getenv('CONFLUENCE_API_LABEL')
token = os.getenv('CONFLUENCE_API_TOKEN')


class APIConnection:
    def __init__(self, base_url, db, username, password):
        self.base_url = base_url
        self.headers = {
            "Authorization": "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()
        }
        self.db = db

    def get_user_info(self, username=None):
        endpoint = f"{self.base_url}/rest/api/user"
        params = {"username": username} if username else {}
        response = requests.get(endpoint, headers=self.headers, params=params)
        data = response.json()
        self.db.insert_user_info(data)
        return data

    def get_user_groups(self, username=None):
        endpoint = f"{self.base_url}/rest/api/user/memberof"
        params = {"username": username} if username else {}
        response = requests.get(endpoint, headers=self.headers, params=params)
        data = response.json()
        user_id = self.get_user_info(username)["id"]
        self.db.insert_user_groups(user_id, data)
        return data

    def add_content_watcher(self, content_id, username=None):
        endpoint = f"{self.base_url}/rest/api/user/watch/content/{content_id}"
        params = {"username": username} if username else {}
        response = requests.post(endpoint, headers=self.headers, params=params)
        return response.status_code  # Returns 204 if successful

    def delete_content_watcher(self, content_id, username=None):
        endpoint = f"{self.base_url}/rest/api/user/watch/content/{content_id}"
        params = {"username": username} if username else {}
        response = requests.delete(endpoint, headers=self.headers, params=params)
        return response.status_code  # Returns 204 if successful

    def is_watching_content(self, content_id, username=None):
        endpoint = f"{self.base_url}/rest/api/user/watch/content/{content_id}"
        params = {"username": username} if username else {}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return response.json()  # Returns {"watching": true/false}

    def get_content_by_id(self, content_id):
        endpoint = f"{self.base_url}/rest/api/content/{content_id}"
        response = requests.get(endpoint, headers=self.headers)
        data = response.json()
        self.db.insert_content(data)
        return data

    def search_content(self, cql):
        endpoint = f"{self.base_url}/rest/api/content/search"
        params = {"cql": cql}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return response.json()

    def search_blogs_in_space(self, space_key, title=None):
        endpoint = f"{self.base_url}/rest/api/content/search"
        cql = f"type=blog and space.key={space_key}"
        if title:
            cql += f" and title~'{title}'"
        params = {"cql": cql}
        response = requests.get(endpoint, headers=self.headers, params=params)
        results = response.json()

        # Handle pagination
        while "next" in response.json()["links"]:
            response = requests.get(response.json()["links"]["next"], headers=self.headers)
            results["results"].extend(response.json()["results"])

        return results

    def get_readable_user_info(self, username):
        data = self.get_user_info(username)
        return json.dumps(data, indent=4)

    def get_readable_user_groups(self, username):
        data = self.get_user_groups(username)
        return json.dumps(data, indent=4)

    def get_readable_content_by_id(self, content_id):
        data = self.get_content_by_id(content_id)
        return json.dumps(data, indent=4)

    def get_readable_blogs_in_space(self, space_key, title=None):
        data = self.search_blogs_in_space(space_key, title)
        return json.dumps(data, indent=4)

