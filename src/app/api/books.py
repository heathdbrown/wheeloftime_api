from app.api import crud
from app.api.models import BookDB, BookSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/", response_model=BookDB, status_code=201)
async def create_book(payload: BookSchema):
    book_id = await crud.post(payload)
    response_object = {
        "id": book_id,
        "title": payload.title,
        "authors": payload.authors,
    }
    return response_object

@router.get("/{id}/", response_model=BookDB)
async def read_book(id: int):
    book = await crud.get(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book