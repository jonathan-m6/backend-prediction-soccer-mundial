from pydantic import BaseModel

class user(BaseModel):
  _id: str | None = None
  email: str
  username: str