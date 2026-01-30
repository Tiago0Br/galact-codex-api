import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('STAR_WARS_API_URL')

r = requests.get(f'{BASE_URL}/people/1')
print(r.json())