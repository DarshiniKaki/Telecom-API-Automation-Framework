import requests
from utils.config import Config

class BaseAPI:

    def get(self, endpoint, params=None):
        return
requests.get(f"{Config.BASE_URL}
{endpoint}", params=params)

    def post(self, endpoint, data=None,
json=None):
        return
requests.post(f"{Config.BASE_URL}
{endpoint}", data=data, json=json)

    def put(self, endpoint, data=None):
        return
requests.put(f"{Config.BASE_URL}
{endpoint}", data=data)

    def delete(self, endpoint):
        return
requests.delete(f"{Config.BASE_URL}
{endpoint}")