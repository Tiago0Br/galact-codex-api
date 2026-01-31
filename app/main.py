import requests
from schemas.person import Person
import config

r = requests.get(f'{config.BASE_URL}/people/1')
raw_data = r.json()
person = Person(**raw_data)

print(person.name)
print(person.height)
print(person.gender)
