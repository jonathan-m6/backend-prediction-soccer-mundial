from pydantic import BaseModel

class prediction(BaseModel):
  _id: str | None = None
  eventId: str
  golesVisita: int
  golesLocal: int
  useId: str
  tiemposExtra: bool
  penales: bool