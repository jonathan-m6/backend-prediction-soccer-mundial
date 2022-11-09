from pydantic import BaseModel, Field

class user(BaseModel):
  _id: str
  email: str = Field(...)
  username: str = Field(...)
  puntosResultado: int = Field(default = 0)
  puntosMarcador: int = Field(default = 0)
  total: int = Field(default = 0)
  amigos: list = Field(default = [])
  avatar: str = Field(default=0)