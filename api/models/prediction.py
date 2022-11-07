from pydantic import BaseModel, Field

class prediction(BaseModel):
  _id: str | None = None
  eventId: str = Field(...)
  golesVisita: int
  golesLocal: int
  useId: str = Field(...)
  tiemposExtra: bool
  penales: bool