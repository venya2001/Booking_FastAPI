from app.database.datebase import async_session_maker
from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()