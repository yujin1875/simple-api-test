from api.client.base_client import BaseClient

class PostsClient(BaseClient):
    POSTS_ENDPOINT = "/posts"

    def get_posts(self, params=None):
        return self.get(self.POSTS_ENDPOINT, params=params)

    def get_post(self, post_id):
        return self.get(f"{self.POSTS_ENDPOINT}/{post_id}")

    def create_post(self, payload):
        return self.post(self.POSTS_ENDPOINT, json=payload)

    def update_post(self, post_id, payload):
        return self.put(f"{self.POSTS_ENDPOINT}/{post_id}", json=payload)

    def patch_post(self, post_id, payload):
        return self.patch(f"{self.POSTS_ENDPOINT}/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.delete(f"{self.POSTS_ENDPOINT}/{post_id}")