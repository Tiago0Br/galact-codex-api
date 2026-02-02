import pytest
from app.main import app

@pytest.fixture
def client():
  """Cria um cliente de teste do Flask para simular requisições."""
  with app.test_client() as client:
    yield client