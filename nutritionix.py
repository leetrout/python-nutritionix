import copy
import os

from requests import request

BASE_URL = "https://api.nutritionix.com/v1_1/"


class ImproperlyConfigured(Exception):
    pass


# wrapper object pattern from pivotal-py by @robhudson
class Nutritionix(object):
    def __init__(self, app_id=None, api_key=None):
        env = os.environ
        self.app_id = app_id or env.get('NIX_APP_ID')
        self.api_key = api_key or env.get('NIX_API_KEY')
        self.base_url = BASE_URL
        self.path = []
        self.qs = {}

    def __getattr__(self, method):
        # Create a new copy of self
        obj = self.__class__(self.app_id, self.api_key)
        obj.path = copy.copy(self.path)
        obj.qs = copy.copy(self.qs)

        obj.path.append(method)
        return obj.mock_attr

    def mock_attr(self, *args, **kwargs):
        """
        Empty method to call to slurp up args and kwargs.

        `args` get pushed onto the url path.
        `kwargs` are converted to a query string and appended to the URL.
        """
        self.path.extend(args)
        self.qs.update(kwargs)
        return self

    @property
    def url(self):
        url = self.base_url + '/'.join(map(str, self.path))
        return url

    def set_auth(self):
        if not self.app_id or not self.api_key:
            raise ImproperlyConfigured("Missing app id or api key")
        self.qs.update(
            {"appId": self.app_id, "appKey": self.api_key}
        )

    def get(self):
        self.set_auth()
        return request('get', self.url, params=self.qs)

    def json(self):
        return self.get().json()
