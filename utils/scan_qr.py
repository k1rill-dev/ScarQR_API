from PIL import Image
from pyzbar.pyzbar import decode


def detect_qr(image: Image) -> str:
    """Распознает QR-код и возвращает его содержимого"""

    try:
        result = decode(image)
        return result[0].data
    except:
        return "Не найдены qr коды на фото!"
