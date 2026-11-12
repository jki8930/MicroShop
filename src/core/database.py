from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from .config import settings
from collections.abc import AsyncGenerator


class DatabaseHelper:

    def __init__(self, url: str, echo: bool = False):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)