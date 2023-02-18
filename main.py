import io
import PIL.Image as Image
from fastapi import FastAPI
from utils import detect_qr
import base64
from schemas import Qr, URL
from utils import Predict
from utils import check_ssl, check_redirect, count_https, count_http

app = FastAPI()

@app.post("/phishing")
async def phising_url(url: URL) -> dict:
    predict = Predict(url=url.url).predict_url()
    ssl = check_ssl(url.url)
    redirect = check_redirect(url.url)
    is_http = True if count_http(url.url) > 0 else False
    is_https = True if count_https(url.url) > 0 else False

    return {
        "success": True,
        "predict": predict[0],
        "ssl": ssl,
        "redirect": redirect,
        "is_http": is_http,
        "is_https": is_https
    }


@app.post("/check_qr")
async def check_qr_post(qr: Qr) -> dict:
    byte_decoded = base64.b64decode(qr.file)
    image = Image.open(io.BytesIO(byte_decoded))
    value: str = detect_qr(image)

    return {"success": True,
            "data": value}


@app.get("/")
async def hello() -> dict:
    return {'hello': 'дайте деняк(((((((((('}


@app.get("/check_qr")
async def check_qr_get() -> dict:
    return {"success": True}
