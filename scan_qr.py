from PIL import Image
from pyzbar.pyzbar import decode



def detect_qr(filename: str) -> str:
    try:
        result = decode(Image.open(filename))
        return result[0].data
    except:
        return "Не найдены qr коды на фото!"


# print(detect_qr('sticker.png'))
import os
import io
import PIL.Image as Image

from array import array

def readimage(path):
    # count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

bytes = readimage("D:\python_projects\qr\qr.jpg")
image = Image.open(io.BytesIO(bytes))
image.save('a.png')
