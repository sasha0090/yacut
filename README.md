# Укротитель ссылок (/≧▽≦)/
 ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

Все просто, сокращаем ссылки ассоциируя длинную пользовательскую с короткой, которую предлагает сам пользователь или предоставляет сервис.

Можно использовать как веб-морду, так и апи.


## Запуск проекта

◾ Клонируйте репозиторий и перейти в него

◾ Установите и активируйте виртуальное окружение

◾ Установите зависимости из файла requirements.txt :
```
pip install -r requirements.txt
```
◾ Через командную строку запустите проект:
```
flask run
```

## API
API доступен всем желающим.У сервиса есть только два эндпоинта:

🔷 `/api/id/`
> POST-запрос на создание новой короткой ссылки
 
&nbsp;

🔷 `/api/id/<short_id>/`
> GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации openapi.yml

## Автор

[Александр Телепин](https://github.com/sasha0090)