from flask import Blueprint, jsonify
import logging
from dao.dao import PostsDAO

api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDAO('./data/posts.json', './data/comments.json')
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info(f'Запрос /api/posts/')
    return jsonify(posts.load_posts_json())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'Запрос /api/posts/{postid}')
    return jsonify(posts.get_post_by_pk_json(postid))
