from pydantic import BaseModel, Field

class user(BaseModel):
  _id: str | None = None
  email: str = Field(...)
  username: str = Field(...)