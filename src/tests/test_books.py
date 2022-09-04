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