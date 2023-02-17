import io
import PIL.Image as Image
from fastapi import FastAPI
from scan_qr import detect_qr
from pydantic import BaseModel as PydanticBaseModel
import base64
import joblib



class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Qr(BaseModel):
    file: str


app = FastAPI()




@app.post("/check_qr")
async def check_qr_post(qr: Qr):
    byte_decoded = base64.b64decode(qr.file)
    image = Image.open(io.BytesIO(byte_decoded))
    value: str = detect_qr(image)

    return {"success": True,
            "data": value}

@app.post("/")
async def hello():
    return {'hello': 'hello'}

@app.get("/check_qr")
async def check_qr_get():
    return {"success": True}
