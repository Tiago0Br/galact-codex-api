import requests
from typing import List, Optional, Dict, Any
from app.schemas.person import Person
from app.schemas.planet import Planet
from app.schemas.starship import Starship
from app.schemas.film import Film
import app.config as config

class SwapiService:
  BASE_URL = config.BASE_URL

  @staticmethod
  def _fetch_data(endpoint: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Método auxiliar genérico para buscar dados.
    Trata paginação básica ou retorna apenas os resultados da query.
    """
    try:
      url = f"{SwapiService.BASE_URL}/{endpoint}"
      response = requests.get(url, params=params, timeout=10) 
      response.raise_for_status()

      data = response.json()
      return data.get("results", [])
        
    except requests.RequestException as e:
      print(f"Erro ao conectar na SWAPI: {e}")
      return []

  @staticmethod
  def get_people(search: Optional[str] = None) -> List[Person]:
    params = {"search": search} if search else {}
    raw_data = SwapiService._fetch_data("people", params)
    return [Person(**item) for item in raw_data]

  @staticmethod
  def get_planets(search: Optional[str] = None) -> List[Planet]:
    params = {"search": search} if search else {}
    raw_data = SwapiService._fetch_data("planets", params)
    return [Planet(**item) for item in raw_data]

  @staticmethod
  def get_starships(search: Optional[str] = None) -> List[Starship]:
    params = {"search": search} if search else {}
    raw_data = SwapiService._fetch_data("starships", params)
    return [Starship(**item) for item in raw_data]

  @staticmethod
  def get_films(search: Optional[str] = None) -> List[Film]:
    params = {"search": search} if search else {}
    raw_data = SwapiService._fetch_data("films", params)
    return [Film(**item) for item in raw_data]