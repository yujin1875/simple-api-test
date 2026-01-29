from api.client.base_client import BaseClient

class PostsClient(BaseClient):
    
    """
    /posts API 전용 Client
    - posts 관련 엔드포인트만 담당
    """
    
    POSTS_ENDPOINT = "/posts"

    def get_posts(self, params=None):
        # 전체 게시글 조회
        return self.get(self.POSTS_ENDPOINT, params=params)

    def get_post(self, post_id):
        # 특정 게시글 조회
        return self.get(f"{self.POSTS_ENDPOINT}/{post_id}")

    def create_post(self, payload):
        # 게시글 생성
        return self.post(self.POSTS_ENDPOINT, json=payload)

    def update_post(self, post_id, payload):
        # 게시글 전체 수정
        return self.put(f"{self.POSTS_ENDPOINT}/{post_id}", json=payload)

    def patch_post(self, post_id, payload):
        # 게시글 부분 수정
        return self.patch(f"{self.POSTS_ENDPOINT}/{post_id}", json=payload)

    def delete_post(self, post_id):
        # 게시글 삭제
        return self.delete(f"{self.POSTS_ENDPOINT}/{post_id}")