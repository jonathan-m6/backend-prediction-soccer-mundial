from pydantic import BaseModel

class prediction(BaseModel):
  _id: str
  nombre: str
  equipoLocal: str
  equipoVisita: str
  ronda: int
  fecha: str
  liga: str
  golesLocal: int
  golesVisita: int
  estadio: str
  estado: str
  nombreLocal: str
  nombreVisita: str
  isoLocal: str
  isoVisita: str
  versus: str