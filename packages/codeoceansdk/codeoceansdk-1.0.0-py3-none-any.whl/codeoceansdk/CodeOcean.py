import logging
from dataclasses import dataclass, asdict

import requests

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class CodeOcean:
    """Class to access Code Ocean environment, passing domain and API key"""

    domain: str
    """Code Ocean domain (for example, acmecorp.codeocean.com)"""
    api_key: str
    """API key to use to access capsules."""

    def __post_init__(self):
        self.session = requests.Session()
        self.session.auth = (self.api_key, "")
        self.api_url = f"https://{self.domain}/api/v1"

    def check_domain(self):
        """
        Check if domain is accessible
        :return: bool
        """
        try:
            res = self.session.get(self.api_url)
            logger.debug(res)
            return True
        except requests.ConnectionError as e:
            logger.error(e)
            return False

    @staticmethod
    def _handle_http(res):
        if 199 < res.status_code < 300:
            return res
        elif 399 < res.status_code < 500:
            logger.error(f"Client error! HTTP response: {res.status_code}")
        elif 499 < res.status_code < 600:
            logger.error(f"Server error! HTTP response {res.status_code}")
        else:
            logger.error(f"Unexpected server code! HTTP response {res.status_code}")

        if "message" in res.json():
            logger.error(f"Unsuccessful request: {res.json()['message']}")
        raise requests.HTTPError

    def get(self, url, params=None):
        """
        Handle get requests and errors.
        :param params: Parameters to send in query string.
        :param url: Input url
        :return: requests object
        """
        return self._handle_http(self.session.get(url, params=params))

    def post(self, url, json=None):
        """
        Handle post requests and errors.
        :param json: Dictionary containing JSON parameters.
        :param url: Input url
        :return: requests object
        """
        return self._handle_http(self.session.post(url, json=json))

    def delete(self, url, params=None):
        """
        Handle delete requests and errors.
        :param params: Parameters to send in query string.
        :param url: Input url
        :return: requests object
        """
        return self._handle_http(self.session.delete(url, params=params))

    def put(self, url, json=None):
        """
        Handle put requests and errors.
        :param json: Dictionary containing JSON parameters.
        :param url: Input url
        :return: requests object
        """
        return self._handle_http(self.session.put(url, json=json))

    def patch(self, url, params=None):
        """
        Handle path requests and errors.
        :param params: Parameters to send in query string.
        :param url: Input url
        :return: requests object
        """
        return self._handle_http(self.session.patch(url, params=params))
