from pydantic import BaseModel, Field

class user(BaseModel):
  _id: str
  email: str = Field(...)
  username: str = Field(...)