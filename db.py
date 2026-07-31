from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost:5432/participants"
)

async_session = async_sessionmaker(engine=engine, expire_on_commit=False)
