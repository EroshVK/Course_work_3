import json
from dao.post import Post


class PostsDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            new_posts =[]
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
        return new_posts


posts = PostsDAO('./data/posts.json', './data/comments.json')

print(posts.load_posts())
