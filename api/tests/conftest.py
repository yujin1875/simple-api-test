import pytest
from api.client.posts_client import PostsClient


@pytest.fixture
def posts_client():
    """
    Posts API 테스트에서 공통으로 사용하는 Client Fixture
    """
    return PostsClient()
