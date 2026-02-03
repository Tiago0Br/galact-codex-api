import pytest
from app.services.swapi import SwapiService

@pytest.mark.live
def test_live_swapi_connection():
  """
  Teste end-to-end que valida a conexão com a API do Swapi
  """
  try:
    results = SwapiService.get_people(search="Luke")
    
    assert len(results) > 0
    luke = results[0]
    assert luke.name == "Luke Skywalker"
    assert isinstance(luke.height, int) 
      
  except Exception as e:
    pytest.fail(f"Falha na conexão real com a SWAPI: {e}")