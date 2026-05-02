import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
SERP_KEY = os.getenv("SERP_API_KEY")