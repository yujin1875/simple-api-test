from api.client.posts_client import PostsClient

def test_get_posts_success():
    client = PostsClient()
    
    # 게시글 목록 조회 API 호출
    response = client.get_posts()
    
    # HTTP 상태 코드 검증
    assert response.status_code == 200
    
    # 응답이 JSON 배열인지 확인
    assert isinstance(response.json(), list)
    
    # 게시글이 최소 1개 이상 있는지 확인
    assert len(response.json()) > 0