from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_FILENAME = os.environ.get('MODEL_FILENAME')

print(MODEL_PATH := os.path.join(BASE_DIR, MODEL_FILENAME))
