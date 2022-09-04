from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    authors: str

class BookDB(NoteSchema):
    id: int