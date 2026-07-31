from fastapi import FastAPI
from message import pick_winner

app = FastAPI(title="lottery")


@app.get("/")
async def users():
    return {"message": "will be later"}


@app.get("/start_lottery")
def start_l():
    pick_winner()
    return


@app.post("winner")
def set_winner(winner: None | str):
    return winner
