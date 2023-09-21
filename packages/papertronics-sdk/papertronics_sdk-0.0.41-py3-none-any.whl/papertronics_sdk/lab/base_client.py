import logging

import httpx
from httpx import Client

from .exceptions.status_exception import StatusException

logger = logging.getLogger(__name__)


def http_request(func):
    def wrap(self, url, include_token=True, **kwargs):
        logger.info(f"{str(func.__name__).split(':')[-1]} {url}")
        try:
            url = f"{self.url}{url}"
            if include_token:
                if self.token is None:
                    raise Exception("Client is not Authenticated")
                kwargs["headers"] = kwargs.get("headers", {})
                kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
            response = func(self, url, **kwargs)
            if response.status_code != 200:
                raise StatusException.from_response(response)
        except Exception as e:
            logger.error(f"{func.__name__} {url} {e}")
            raise e
        return response

    return wrap


class BaseClient(Client):

    def __init__(self, url, token=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.token = token

    @staticmethod
    @http_request
    def get(url, **kwargs):
        return super().get(url, **kwargs)

    @staticmethod
    @http_request
    def post(url, **kwargs):
        return super().post(url, **kwargs)

    @staticmethod
    @http_request
    def delete(url, **kwargs):
        return super().delete(url, **kwargs)
