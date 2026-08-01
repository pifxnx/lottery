from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean


class Base(DeclarativeBase):
    pass


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost:5432/participants"
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
