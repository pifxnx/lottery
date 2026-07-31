from db import async_session
from model import ParticipantCreate
from db import Participant
from typing import List
from sqlalchemy import select


async def add_participant(participant: ParticipantCreate):
    async with async_session() as s:
        db_participant = Participant(name=participant.name)
        s.add(db_participant)
        await s.commit()
        await s.refresh(db_participant)

        return db_participant


async def get_participant_by_id(id: int):
    async with async_session() as s:
        participant = await s.get(Participant, id)

        return participant


async def get_all_participants() -> List[Participant]:
    async with async_session() as s:
        query = select(Participant)
        ps = await s.execute(query)
        result = ps.scalars().all()

        return list(result)
