
from flask import json
from flask.globals import request


def test_get_all_books_with_no_records(client):
    response = client.get('/books')
    response_body = response.get_json()

    assert response.status_code ==200
    assert response_body == []

def test_get_book_by_id(client,two_saved_books):
    response = client.get('/books/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "title":"Ocean Book",
        "description":"watr 4evr"
    }

def test_get_by_id_without_data(client):
    response = client.get('/books/1')
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_all_books_with_data(client,two_saved_books):
    response = client.get('/books')
    response_body = response.get_json()

    assert response.status_code ==200
    assert response_body == [{
        "id":1,
        "title":"Ocean Book",
        "description":"watr 4evr"
    },
    {
        "id":2,
        "title":"Mountain Book",
        "description":"i luv 2 climb rocks"
    }]

def test_post_one_book(client):
    json = {
        "id":1,
        "title":"Ocean Book",
        "description":"watr 4evr"
    }
    response = client.post('/books',json= {"id":1,"title":"Ocean Book","description":"watr 4evr"})
    response_body = response.get_json()

    assert response.status_code ==201








