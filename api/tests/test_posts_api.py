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

def test_create_post_success():
    client = PostsClient()
    
    # 게시글 생성 요청에 사용할 payload 정의
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = client.create_post(payload)

    assert response.status_code == 201
    
    # 응답 body를 JSON 형태로 파싱
    response_body = response.json()
    
    # 요청 데이터 반영되었는지 확인
    assert response_body["title"] == payload["title"]
    assert response_body["body"] == payload["body"]
    assert response_body["userId"] == payload["userId"]
    
    # 서버에서 생성한 id 필드가 존재하는지 확인
    assert "id" in response_body

def test_update_post_with_put():
    client = PostsClient()
    payload = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    response = client.update_post(post_id=1, payload=payload)

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]


def test_update_post_with_patch():
    client = PostsClient()
    payload = {
        "title": "patched title"
    }

    response = client.patch_post(post_id=1, payload=payload)

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]
    
def test_delete_post_success():
    client = PostsClient()

    response = client.delete_post(post_id=1)

    assert response.status_code == 200