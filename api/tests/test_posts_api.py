def test_get_posts_success(posts_client):
    
    # 게시글 목록 조회 API 호출
    response = posts_client.get_posts()
    
    # HTTP 상태 코드 검증
    assert response.status_code == 200, "게시글 목록 조회 API가 200을 반환하지 않음"
    
    # 응답이 JSON 배열인지 확인
    assert isinstance(response.json(), list), "게시글 목록 응답이 list 타입이 아님"
    
    # 게시글이 최소 1개 이상 있는지 확인
    assert len(response.json()) > 0, "게시글 목록이 비어 있음"

def test_create_post_success(posts_client):

    # 게시글 생성 요청에 사용할 payload 정의
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = posts_client.create_post(payload)

    assert response.status_code == 201, "게시글 생성 API가 201을 반환하지 않음"
    
    # 응답 body를 JSON 형태로 파싱
    response_body = response.json()
    
    # 요청 데이터 반영되었는지 확인
    assert response_body["title"] == payload["title"], "title 필드가 요청 값과 다름"
    assert response_body["body"] == payload["body"], "body 필드가 요청 값과 다름"
    assert response_body["userId"] == payload["userId"], "userId 필드가 요청 값과 다름"
    
    # 서버에서 생성한 id 필드가 존재하는지 확인
    assert "id" in response_body, "응답에 id 필드가 존재하지 않음"

def test_update_post_with_put(posts_client):

    payload = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    response = posts_client.update_post(post_id=1, payload=payload)

    assert response.status_code == 200, "게시글 PUT 수정 API가 200을 반환하지 않음"
    assert response.json()["title"] == payload["title"], "PUT 수정 후 title 값이 변경되지 않음"


def test_update_post_with_patch(posts_client):

    payload = {
        "title": "patched title"
    }

    response = posts_client.patch_post(post_id=1, payload=payload)

    assert response.status_code == 200, "게시글 PATCH 수정 API가 200을 반환하지 않음"
    assert response.json()["title"] == payload["title"], "PATCH 수정 후 title 값이 변경되지 않음"
    
def test_delete_post_success(posts_client):

    response = posts_client.delete_post(post_id=1)

    assert response.status_code == 200, "게시글 삭제 API가 200을 반환하지 않음"