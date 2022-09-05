import json
import pytest
from app.api import crud

def test_create_book(test_app, monkeypatch):
    test_request_payload = {"title": "The Eye of the World", "authors": "Robert Jordan"}
    test_response_payload = {"id": 1, "title": "The Eye of the World", "authors": "Robert Jordan"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/books/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload

def test_create_book_invalid_json(test_app):
    response = test_app.post("/books/", data=json.dumps({"title": "The Eye of the World"}))
    assert response.status_code == 422

def test_read_book(test_app, monkeypatch):
    test_data = {"id": 1, "title": "The Eye of the World", "authors": "Robert Jordan"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/books/1")
    assert response.status_code == 200
    assert response.json() == test_data

def test_read_book_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/books/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

def test_read_all_books(test_app, monkeypatch):
    test_data = [
        {"title": "The Eye of the World", "authors": "Robert Jordan", "id": 1},
        {"title": "The Great Hunt", "authors": "Robert Jordan", "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/books/")
    assert response.status_code == 200
    assert response.json() == test_data