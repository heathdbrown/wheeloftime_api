from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    authors: str

class BookDB(BookSchema):
    id: int