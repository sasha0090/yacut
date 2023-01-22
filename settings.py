import os
import string

MAX_LEN_USER_CUSTOM_ID = 16
GEN_LEN_CUSTOM_ID = 6

ALLOWED_CHARACTERS = (
        string.ascii_lowercase + string.ascii_uppercase + string.digits
)


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
