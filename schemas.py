from pydantic import BaseModel


class TemperatureSchema(BaseModel):
    id: int
    value: float
    created_at: str


class WindVelocitySchema(BaseModel):
    id: int
    value: float
    created_at: str