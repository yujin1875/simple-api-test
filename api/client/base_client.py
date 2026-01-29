import requests
from config.settings import BASE_URL

class BaseClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None):
        return requests.get(
            url=f"{self.base_url}{endpoint}",
            params=params
        )

    def post(self, endpoint, json=None):
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            json=json
        )

    def put(self, endpoint, json=None):
        return requests.put(
            url=f"{self.base_url}{endpoint}",
            json=json
        )

    def patch(self, endpoint, json=None):
        return requests.patch(
            url=f"{self.base_url}{endpoint}",
            json=json
        )

    def delete(self, endpoint):
        return requests.delete(
            url=f"{self.base_url}{endpoint}"
        )