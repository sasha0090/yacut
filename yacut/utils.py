import secrets

from settings import GEN_LEN_CUSTOM_ID, ALLOWED_CHARACTERS as ALLCHAR
import random

from . import db
from yacut.models import URLMap


def get_unique_short_id(len_symbols=GEN_LEN_CUSTOM_ID):
    return ''.join(secrets.choice(ALLCHAR) for _ in range(len_symbols))


def create_url_map(original_link, custom_id=None):
    url_map = URLMap.query.filter_by(original=original_link).first()

    if not url_map or custom_id and url_map:
        if not custom_id:
            custom_id = get_unique_short_id()

        url_map = URLMap(short=custom_id, original=original_link)
        db.session.add(url_map)
        db.session.commit()

    return url_map
