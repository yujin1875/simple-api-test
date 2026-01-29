from api.client.posts_client import PostsClient

def test_get_posts_success():
    client = PostsClient()
    
    response = client.get_posts()
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0