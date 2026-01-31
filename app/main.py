import os
import requests
from dotenv import load_dotenv
from schemas.person import Person

load_dotenv()

BASE_URL = os.getenv('STAR_WARS_API_URL')

r = requests.get(f'{BASE_URL}/people/1')
raw_data = r.json()
person = Person(**raw_data)

print(person.name)
print(person.height)
print(person.gender)
