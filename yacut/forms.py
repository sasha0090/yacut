from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Regexp

from settings import MAX_LEN_USER_CUSTOM_ID


class CutForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
            URL(message='Должна быть ссылка')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(0, MAX_LEN_USER_CUSTOM_ID),
            Regexp(
                '[0-9A-Za-z]*',
                message='Используйте только:'
                        ' большие латинские буквы,'
                        ' маленькие латинские буквы,'
                        ' цифры в диапазоне от 0 до 9.'
            )
        ],
    )
    submit = SubmitField('Создать')
