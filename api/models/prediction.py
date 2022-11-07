from pydantic import BaseModel


class prediction(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None