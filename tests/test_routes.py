from app.schemas.person import Person

MOCK_PERSON = Person(
  name="Han Solo",
  height=180,
  mass=80,
  hair_color="brown",
  skin_color="fair",
  eye_color="brown",
  birth_year="29BBY",
  gender="male",
  films=[]
)

def test_route_people_success(client, mocker):
  """Testa se a rota /people retorna 200 e JSON correto."""

  mocker.patch(
    "app.services.swapi.SwapiService.get_people",
    return_value=[MOCK_PERSON]
  )

  response = client.get("/people")

  assert response.status_code == 200
  data = response.get_json()
  
  assert len(data) == 1

  print(data)

  assert data[0]["name"] == "Han Solo"
  assert data[0]["height"] == 180

def test_route_not_found(client):
  """Testa uma rota que não existe."""
  response = client.get("/rota-inexistente")
  assert response.status_code == 404