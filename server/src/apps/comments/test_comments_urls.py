import requests
from django.core import mail

ENDPOINT = 'http://127.0.0.1:8000/library/books/izuchaem-python20221219061671440801/comments/'


def test_get_comments_list():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200

    print(response.json())


def test_comments_add():
    payload = {
      "book": "izuchaem-python20221219061671440801",
      "content": "string",
      "parent": 0
    }

    response = requests.post(ENDPOINT+"/add/", json=payload)

    assert response.status_code == 201

    print(response.json())


def test_comment_get_by_id():
    response = requests.get(ENDPOINT + "/1")

    assert response.status_code == 200

    print(response.json())


def test_get_comment_likes():
    response = requests.get(ENDPOINT + "/1/like")

    assert response.status_code == 200

    print(response.json())






