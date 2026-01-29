import logging
import logging.config
import requests
from api.config.settings import BASE_URL, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class BaseClient:

    def _request(self, method, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"

        logger.info("API Request")
        logger.info("METHOD=%s URL=%s", method, url)

        if "json" in kwargs:
            logger.info("PAYLOAD=%s", kwargs["json"])

        response = requests.request(method, url, **kwargs)

        logger.info("API Response")
        logger.info("STATUS=%s", response.status_code)
        logger.debug("BODY=%s", response.text)

        return response

    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, json=None):
        return self._request("POST", endpoint, json=json)

    def put(self, endpoint, json=None):
        return self._request("PUT", endpoint, json=json)

    def patch(self, endpoint, json=None):
        return self._request("PATCH", endpoint, json=json)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)
