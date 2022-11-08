from pydantic import BaseModel, Field

class prediction(BaseModel):
  _id: str
  eventId: str = Field(...)
  golesVisita: int
  golesLocal: int
  userId: str = Field(...)
  tiemposExtra: bool = Field(default=False)
  penales: bool = Field(default=False)