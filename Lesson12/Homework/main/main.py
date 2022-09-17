from flask import Blueprint, render_template, request
import functions as f
import logging

main_blueprint = Blueprint('main_blueprint', __name__)
posts = "posts.json"
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Logger')


@main_blueprint.route('/', methods=['POST', 'GET'])
def get_main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_word():
    all_posts: list[dict] = f.load_posts(posts)
    word = request.args.get('s')
    posts_with_word: list[dict] = f.get_post(all_posts, word)
    logger.info("Произведен поиск постов")
    return render_template("post_list.html", posts_with_word=posts_with_word, word=word, title=word)
