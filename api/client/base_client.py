import logging
import logging.config
import requests
from api.config.settings import BASE_URL, LOGGING_CONFIG

# 로깅 설정 로드
logging.config.dictConfig(LOGGING_CONFIG)
# 현재 모듈 기준 로거 생성
logger = logging.getLogger(__name__)


class BaseClient:
    
    """
    모든 API Client의 부모 클래스
    - HTTP 요청 공통 처리
    - 로깅 공통 처리
    """
    
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
