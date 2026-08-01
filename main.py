from fastapi import FastAPI
from message import pick_winner
from model import ParticipantCreate
from crud import (
    get_all_participants,
    get_participant_by_id,
    add_participant,
    get_winner,
    set_winner,
    clean_table,
)

app = FastAPI(title="lottery")


@app.get("/")
async def users():
    return {"message": "will be later"}


@app.post("/start_lottery")
def start_l():
    pick_winner()
    return {"message": "лотерея запущена"}


@app.post("/add")
async def add(participant: ParticipantCreate):
    return await add_participant(participant)


@app.get("/participants")
async def get_ps():
    res = await get_all_participants()
    return res


@app.get("/participants/{id}")
async def get_ps_by_id(id: int):
    res = await get_participant_by_id(id)
    return res


@app.post("/choose_winner")
async def winner():
    participant = await set_winner()
    return participant


@app.get("/get_winner")
async def show_winner():
    participant = await get_winner()
    return participant


@app.post("/participants/clear")
async def truncate():
    await clean_table()
    return {"message": "таблица очищена"}
