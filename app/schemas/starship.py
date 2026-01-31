from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class Starship(BaseModel):
  name: str
  model: str
  manufacturer: str
  cost_in_credits: Optional[float] = Field(None, description="Custo em créditos galácticos")
  length: Optional[float] = Field(None, description="Comprimento da nave")
  hyperdrive_rating: str
  crew: str
  passengers: str
  films: List[str]

  @field_validator('cost_in_credits', 'length', mode='before')
  def parse_numbers(cls, v):
    if isinstance(v, str):
      clean_v = v.replace(',', '').replace('.', '', 1)
      if clean_v.isnumeric():
        return float(v.replace(',', ''))
      return None