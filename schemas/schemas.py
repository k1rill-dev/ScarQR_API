from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Qr(BaseModel):
    file: str


class URL(BaseModel):
    url: str
