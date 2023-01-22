import re

from settings import MAX_LEN_USER_CUSTOM_ID
from . import app, db
from flask import jsonify, request, url_for

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import create_url_map


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    original_link = data['url']
    custom_id = data.get('custom_id')

    if custom_id:
        if len(custom_id) > MAX_LEN_USER_CUSTOM_ID:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

        if not re.match("^[0-9A-Za-z]*$", custom_id):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(f'Имя \"{custom_id}\" уже занято.')

    url_map = create_url_map(original_link, custom_id)

    short_link = url_for(
        'short_url_view',
        custom_id=url_map.short,
        _external=True
    )
    return jsonify({"url": original_link, "short_link": short_link}), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()

    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', 404)

    return jsonify({"url": url_map.original}), 200








