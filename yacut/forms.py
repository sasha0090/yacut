from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length, Regexp

from settings import MAX_LEN_USER_CUSTOM_ID, TEXT_INVALID_NAME, TEXT_NOT_URL


class CutForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(1, 256),
            URL(message=TEXT_NOT_URL),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(0, MAX_LEN_USER_CUSTOM_ID),
            Regexp(
                "[0-9A-Za-z]*",
                message=TEXT_INVALID_NAME,
            ),
        ],
    )
    submit = SubmitField("Создать")
