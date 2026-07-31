from fastapi import FastAPI
from message import pick_winner
from model import ParticipantCreate
from schemas import get_all_participants, get_participant_by_id, add_participant

app = FastAPI(title="lottery")


@app.get("/")
async def users():
    return {"message": "will be later"}


@app.get("/start_lottery")
def start_l():
    pick_winner()
    return


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


@app.post("winner")
def set_winner(winner: None | str):
    return winner
