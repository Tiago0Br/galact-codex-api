from unittest.mock import Mock
from app.services.swapi import SwapiService

MOCK_SWAPI_RESPONSE = {
  "results": [
    {
      "title": "A New Hope",
			"episode_id": 4,
			"opening_crawl": "It is a period of civil war.",
			"director": "George Lucas",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1977-05-25",
      "characters": [
        "https://swapi.dev/api/people/1/"
      ]
    }
  ]
}

def test_get_film_success(mocker):
  """
  Testa se o service busca e converte os dados corretamente
  """
  mock_get = mocker.patch("app.services.swapi.requests.get")

  mock_response = Mock()
  mock_response.json.return_value = MOCK_SWAPI_RESPONSE
  mock_response.status_code = 200
  mock_get.return_value = mock_response

  film = SwapiService.get_films()

  assert len(film) == 1
  film = film[0]

  assert film.title == "A New Hope"
  assert film.episode_id == 4

  mock_get.assert_called_once()
  assert "film" in mock_get.call_args[0][0]