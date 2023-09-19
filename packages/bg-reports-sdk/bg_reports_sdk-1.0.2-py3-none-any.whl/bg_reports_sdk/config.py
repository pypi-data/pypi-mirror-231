import os

from dotenv import load_dotenv

load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST", "https://app-backend.focustech.xyz")
MASTER_TOKEN = os.getenv("MASTER_TOKEN")
