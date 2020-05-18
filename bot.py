import os
import sys
import random
import environ
import requests
import mimesis


directory = os.path.dirname(__file__)
default_dotenv_path = os.path.join(directory, '.env')


def read_config(path):
    env = environ.Env()
    env.read_env(env_file=path)
    return env


def get_dotenv_path():
    if '--env-file' not in sys.argv:
        dotenv_path = default_dotenv_path
    else:
        idx = sys.argv.index('--env-file')
        if len(sys.argv) < idx:
            dotenv_path = default_dotenv_path
        else:
            dotenv_path = sys.argv[idx + 1]

    return dotenv_path


def get_headers(access):
    return {'Authorization': f'Bearer {access}'}


def signup_user(url, password):
    person = mimesis.Person('ru')
    data = {
        'username': person.username(),
        'email': person.email(),
        'password': password
    }
    requests.post(url + 'api/user/signup', json=data)

    auth_payload = {
        'username': data['username'],
        'password': data['password']
    }
    data['access'] = requests.post(url + 'api/auth/obtain', json=auth_payload).json()['access']

    return data


def make_post(url, user_data):
    post_data = {
        'text': mimesis.Text().text()
    }
    response = requests.post(url + 'api/posts', json=post_data, headers=get_headers(user_data['access'])).json()
    post_data['id'] = response['id']

    return post_data


def like_post(url, user_data, post_id):
    requests.post(url + f'api/posts/{post_id}/like', headers=get_headers(user_data['access']))


def main():
    dotenv_path = get_dotenv_path()
    env = read_config(dotenv_path)

    url = env.str('url', default='http://localhost:8000/')
    number_of_users = env.int('number_of_users', 5)
    max_posts_per_user = env.int('max_posts_per_user', 5)
    max_likes_per_user = env.int('max_likes_per_user', 5)
    user_password = env.str('password', 'P@ssword1234')

    # signup users
    users = [signup_user(url, user_password) for _ in range(number_of_users)]

    # make posts
    for user_data in users:
        user_data['posts'] = []
        for _ in range(random.randint(0, max_posts_per_user)):
            user_data['posts'].append(make_post(url, user_data))

    all_posts = [post_data for user_data in users for post_data in user_data['posts']]

    # if there is not posts - skip liking stage
    if not all_posts:
        print('WARN: no posts generated')
        return

    # like posts
    for user_data in users:
        for _ in range(random.randint(0, max_likes_per_user)):
            like_post(url, user_data, random.choice(all_posts)['id'])


if __name__ == '__main__':
    main()
