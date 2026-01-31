from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class Planet(BaseModel):
  name: str = Field(..., description="Nome do planeta")
  climate: str
  terrain: str
  population: Optional[int] = Field(None, description="População")
  residents: List[str]
  films: List[str]

  @field_validator('population', mode='before')
  def parse_population(cls, v):
    if isinstance(v, str) and v.isnumeric():
      return int(v)
    return None