# 실패(negative) 시나리오 테스트 모음
# JSONPlaceholder 가 예외 처리가 거의 안되어 있어 다른 상태값을 뱉기도 함
# 로직 구현에만 의의를 두고 작성함

def test_get_post_not_found(posts_client):
    """
    존재하지 않는 게시글 조회 시 동작 확인
    """
    invalid_post_id = 9999

    response = posts_client.get_post(post_id=invalid_post_id)

    assert response.status_code in [404], \
        "존재하지 않는 게시글 조회 시 예상 외 상태 코드 반환"


def test_update_post_not_found(posts_client):
    """
    존재하지 않는 게시글 수정 시 동작 확인
    """
    invalid_post_id = 9999

    payload = {
        "title": "invalid update",
        "body": "invalid update",
        "userId": 1
    }

    response = posts_client.update_post(post_id=invalid_post_id, payload=payload)

    # JSONPlaceholder는 invalid id에 대해 500을 반환할 수 있음
    # 실제 서비스는 404
    assert response.status_code in [404, 500], \
        "존재하지 않는 게시글 수정 시 예상 외 상태 코드 반환"


def test_delete_post_not_found(posts_client):
    """
    존재하지 않는 게시글 삭제 시 동작 확인
    """
    invalid_post_id = 9999

    response = posts_client.delete_post(post_id=invalid_post_id)

    # JSONPlaceholder는 존재하지 않는 리소스도 200 반환할 수 도 있다.
    # 실제 서비스는 200, 202, 204, 404
    assert response.status_code in [200, 404], \
        "존재하지 않는 게시글 삭제 시 예상 외 상태 코드 반환"


def test_create_post_with_invalid_payload(posts_client):
    """
    필수 필드가 누락된 payload로 게시글 생성 시 동작 확인
    """
    invalid_payload = {
        "title": "missing body"
        # body, userId 누락
    }

    response = posts_client.create_post(invalid_payload)

    # JSONPlaceholder는 invalid payload에도 201을 반환할 수 도 있다.
    # 실제 서비스는 400
    assert response.status_code in [201, 400], \
        "비정상 payload 처리 방식이 예상과 다름"
