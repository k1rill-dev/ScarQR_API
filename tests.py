# import io
import json
import requests
# from PIL import Image
# import base64
# from scan_qr import detect_qr
#
#
# def readimage(path):
#     # count = os.stat(path).st_size / 2
#     with open(path, "rb") as f:
#         return bytes(f.read())
#
# bytes_ = readimage("D:\python_projects\qr\qr.jpg")
# encoded = base64.b64encode(bytes_)
# print(data := encoded.decode('ascii'))
# decoded = base64.b64decode(data)
# print(requests.post('http://127.0.0.1:8000/phishing', json={
#     "url": "https://github.com/k1rill-dev/ScarQR_API"
# }).json())
import aiohttp
import asyncio
async def lol():
    async with aiohttp.ClientSession() as session:
        data = {'url': "https://github.com/k1rill-dev/ScarQR_API"}
        a = await session.post('http://127.0.0.1:8000/phishing', json=data)
        reult = await a.json(encoding='utf-8')
        print('-------------------->', reult)


asyncio.run(lol())
# print(json.dumps({
#     'file': data
# }))

# from scan_qr import detect_qr
# v = b""
# # bt = v+a.replace('b', '').replace("'", "")
# bt = bytes(a.replace('b', '').replace("'", ""), encoding='ascii')
# image = Image.open(io.BytesIO(decoded))
# print(detect_qr(image))