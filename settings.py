import os
import string

MAX_LEN_USER_CUSTOM_ID = 16
GEN_LEN_CUSTOM_ID = 6

ALLOWED_CHARACTERS = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits
)

TEXT_NOT_URL = "Должна быть ссылка!"

TEXT_INVALID_NAME = "Указано недопустимое имя для короткой ссылки"


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
