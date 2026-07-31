from pydantic import BaseModel, ConfigDict


class ParticipantCreate(BaseModel):
    name: str


class ParticipantResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
