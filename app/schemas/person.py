from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class Person(BaseModel):
  name: str = Field(..., description="Nome do personagem")
  height: Optional[int] = Field(None, description="Altura em cm")
  mass: Optional[float] = Field(None, description="Peso em kg")
  hair_color: str
  skin_color: str
  eye_color: str
  birth_year: str
  gender: str
  films: List[str] 
  
  @field_validator('height', mode='before')
  def parse_height(cls, v):
    if isinstance(v, str) and v.isnumeric():
      return int(v)
    return None

  @field_validator('mass', mode='before')
  def parse_mass(cls, v):
    if isinstance(v, str):
      clean_v = v.replace(',', '.')
      try:
        return float(clean_v)
      except ValueError:
        return None
    return v