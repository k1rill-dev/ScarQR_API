from fastapi import FastAPI
from scan_qr import detect_qr
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Image(BaseModel):
    file: bytearray


app = FastAPI()


@app.post("/check_qr")
async def root(img: Image):

    value: str = detect_qr(img.file)

    return {"success": True,
            "data": value}

