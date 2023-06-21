from typing import Union

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (create_async_engine, AsyncEngine, async_sessionmaker,
                                    AsyncSession)


def get_engine(url: Union[URL, str]) -> AsyncEngine:
    return create_async_engine(url=url, echo=True)


def get_session_maker(engine: AsyncEngine) -> AsyncSession:
    return async_sessionmaker(engine, expire_on_commit=False)
