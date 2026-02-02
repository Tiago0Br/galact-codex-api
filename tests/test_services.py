from unittest.mock import Mock
from app.services.swapi import SwapiService

MOCK_SWAPI_RESPONSE = {
  "results": [
    {
      "name": "Luke Skywalker",
      "height": "172",
      "mass": "77",
      "hair_color": "blond",
      "skin_color": "fair",
      "eye_color": "blue",
      "birth_year": "19BBY",
      "gender": "male",
      "films": ["https://swapi.dev/api/films/1/"]
    }
  ]
}

def test_get_people_success(mocker):
  """
  Testa se o service busca e converte os dados corretamente
  """
  mock_get = mocker.patch("app.services.swapi.requests.get")

  mock_response = Mock()
  mock_response.json.return_value = MOCK_SWAPI_RESPONSE
  mock_response.status_code = 200
  mock_get.return_value = mock_response

  people = SwapiService.get_people(search="Luke")

  assert len(people) == 1
  luke = people[0]

  assert luke.name == "Luke Skywalker"
  assert luke.height == 172 
  assert isinstance(luke.height, int)

  mock_get.assert_called_once()
  assert "people" in mock_get.call_args[0][0]

def test_get_people_empty(mocker):
  """Testa se o service lida bem com lista vazia."""
  mock_get = mocker.patch("app.services.swapi.requests.get")
  mock_response = Mock()
  mock_response.json.return_value = {"results": []}
  mock_get.return_value = mock_response

  people = SwapiService.get_people()
  assert len(people) == 0
  assert isinstance(people, list)