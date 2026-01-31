import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('STAR_WARS_API_URL')
assert BASE_URL is not None, "STAR_WARS_API_URL is not defined"
