import random

from send_request import SendRequest
from api_urls import (
    set_like_or_dislike,
    end_dislike_url,
    end_like_url
)
from send_posts import send_posts
from get_user_token import get_user_token


class addLike(SendRequest):
    def __init__(self, posts, users, method=''):
        super().__init__(method=method)
        self.posts = posts
        self.users = users

    def add_like(self):
        likes = []
        for user in self.users:
            access_token = user["access"]

            for post in self.posts:

                urls = [
                    f"{set_like_or_dislike}{post['id']}{end_like_url}",
                    f"{set_like_or_dislike}{post['id']}{end_dislike_url}",
                ]

                response = self.send_url(
                    url=random.choice(urls),
                    headers={"Authorization": f"Token {access_token}"},
                )
                response['post_id'] = post['id']
                likes.append(response)
        return likes


add_like = addLike(send_posts, get_user_token,
                   method='POST'.upper()).add_like()
