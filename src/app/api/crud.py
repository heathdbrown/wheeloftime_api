from app.api.models import BookSchema
from app.db import books, database

async def post(payload: BookSchema):
    query = books.insert().values(title=payload.title, authors=payload.authors)
    return await database.execute(query=query)