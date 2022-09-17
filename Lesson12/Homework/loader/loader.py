from flask import Blueprint, render_template, request
import functions as f
from json import JSONDecodeError
import logging

posts = "posts.json"
loader_blueprint = Blueprint('loader_blueprint', __name__)
logger = logging.getLogger('Logger')


@loader_blueprint.route('/post', methods=['GET'])
def load_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload', methods=['POST'])
def get_loaded_post():
    pic = request.files.get('picture')
    if pic:
        cont: str = request.form.get('content')
        filename = pic.filename
        if f.check_format(filename):
            pic_path = f'./uploads/images/{filename}'
            try:
                added_post = f.add_post(pic_path, cont, posts)
                pic.save(pic_path)
            except (FileNotFoundError, JSONDecodeError):
                return f'Ошибка записи или файл не найден'
        else:
            logger.info('Попытка загрузить не картинку')
            return f"Данный формат {filename.split('.')[1]} не доступен для добавления"
        return render_template('post_uploaded.html', added_post=added_post)
    logger.error('Ошибка записи файла')
    return f'Файл не загружен'
