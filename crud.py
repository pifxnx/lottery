from db import async_session
from model import ParticipantCreate
from db import Participant
from typing import List
from sqlalchemy import select, func, update, text
from sqlalchemy.ext.asyncio import AsyncSession


async def get_participant_by_id(id: int, s: AsyncSession):
    participant = await s.get(Participant, id)

    return participant


async def get_participant_by_name(name: str, s: AsyncSession):
    stmt = select(Participant).where(Participant.name == name)
    res = await s.execute(stmt)
    participant = res.scalar_one_or_none()
    return participant


async def add_participant(participant: ParticipantCreate, s: AsyncSession):
    if await get_participant_by_name(participant.name, s) is None:
        db_participant = Participant(name=participant.name)
        s.add(db_participant)
        await s.commit()
        await s.refresh(db_participant)

        return db_participant
    else:
        return {"message": "участник с таким именем уже существует"}


async def get_all_participants(s: AsyncSession) -> List[Participant]:
    query = select(Participant)
    ps = await s.execute(query)
    result = ps.scalars().all()

    return list(result)


async def get_winner(s: AsyncSession):
    stmt = select(Participant).where(Participant.status == True)
    res = await s.execute(stmt)
    participant = res.scalar_one_or_none()
    return participant


async def set_winner(s: AsyncSession):
    if await get_winner(s) is None:
        stmt = select(Participant).order_by(func.random()).limit(1)
        res = await s.execute(stmt)
        participant = res.scalar_one()
        stmt = (
            update(Participant)
            .where(Participant.id == participant.id)
            .values(status=True)
        )
        await s.execute(stmt)
        await s.commit()

        return participant
    else:
        return {"message": "победитель уже выбран"}


async def clean_table(s: AsyncSession):
    await s.execute(text("TRUNCATE TABLE participants RESTART IDENTITY"))
    await s.commit()
