from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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
from db import get_db


admin = {"username": "admin", "password": "admin"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="lottery")


@app.post("/token")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    if data.username == admin["username"] and data.password == admin["password"]:
        return {"access_token": "admin", "token_type": "bearer"}


@app.post("/start_lottery")
def start_l(token: str = Depends(oauth2_scheme)):
    if token == "admin":
        pick_winner()
        return {"message": "лотерея запущена"}


@app.post("/add")
async def add(participant: ParticipantCreate, session=Depends(get_db)):
    return await add_participant(participant, session)


@app.get("/participants")
async def get_ps(session=Depends(get_db)):
    res = await get_all_participants(session)
    return res


@app.get("/participants/{id}")
async def get_ps_by_id(id: int, session=Depends(get_db)):
    res = await get_participant_by_id(id, session)
    return res


@app.post("/choose_winner")
async def winner(session=Depends(get_db)):
    participant = await set_winner(session)
    return participant


@app.get("/get_winner")
async def show_winner(session=Depends(get_db)):
    participant = await get_winner(session)
    return participant


@app.post("/participants/clear")
async def truncate(session=Depends(get_db)):
    await clean_table(session)
    return {"message": "таблица очищена"}
