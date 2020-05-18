# Starnavi – тестовое задание
Предполагается, что все команды ниже будут вводится из корня проекта.


Запуск проекта нативно (без docker'а):

```shell script
python -m venv venv
python -m pip install -r requiremnts.txt
cd src
python manage.py migrate
python manage.py runserver
```

Запуск проекта с помощью docker-compose:

```shell script
docker-compose up -d --build
```

В docker-compose помимо контейнера с Python подняты контейнеры с PostgreSQL и Nginx.

Запуск бота:
```shell script
cp .env.example .env
python src/bot.py
```

Конфигурация бота производится с помощью .env файла в корне проекта. 
Для примера приложен файл .env.example. 

Путь до .env файла можно также задать с помощью параметра _--env-file_, например: `python src/bot.py --env-file .env.example`.

 # Описание API
 К проекту приложен дамп Postman-коллекции (v2.1) в качестве документации.
 
 Для авторизации используюся методы:
 - api/auth/obtain – получение access и refresh токенов и 
 - api/auth/refresh – для обновления access и refresh токена по refresh токену.
 
 Время жизни access токена по умолчанию равно 10 минутам.
 Время жизни refresh токена по умолчанию равно 7 дням.
 
 Помимо указанных в задании методов добавлены также методы:
 - api/user – получение данных текущего пользователя
 - api/analytics/users – получение статистики по всем пользователям
 - api/analytics/user/{username} - получение статистики по конкретному пользователю (в задании не был указан url для этого метода)
 
 Методы из раздела analytics требуют правда администратора (поле is_staff). Для создания администратора:
 
```shell script
cd src
python manage.py createsuperuser
```

Или с помощью docker-compose:

```shell script
docker-compose exec back python manage.py createsuperuser
```