import pytest
import requests

# test author
def test_post_author():
    response = requests.post(
        "http://localhost:5000/api/author",
        data={
            "name": "Luan"
            })
    assert response.status_code == 201

def test_get_authors():
    response = requests.get("http://localhost:5000/api/author")
    assert response.status_code == 200

def test_get_author():
    response = requests.get("http://localhost:5000/api/author/Luan")
    assert response.status_code == 200

# test book
def test_post_book():
    response = requests.post(
        "http://localhost:5000/api/book",
        data={
                "name": "Seiquelápamemo",
                "edition": "sei lá",
                "publication_year": "2020",
                "authors": [1, 2, 3]
            })
    assert response.status_code == 201

def test_get_books():
    response = requests.get("http://localhost:5000/api/book")
    assert response.status_code == 200

def test_get_book():
    response = requests.get("http://localhost:5000/api/book/Seiquelápamemo")
    assert response.status_code == 200

# test destroy
def test_destroy():
    try:
        author_response = requests.delete(f"http://localhost:5000/api/author/Luan")
        author_response = requests.delete(f"http://localhost:5000/api/book/Seiquelápamemo")
    except Exception as e:
        print(e)
    assert author_response.status_code == 204
