from pydantic import BaseModel, Field
from typing import List

class Film(BaseModel):
  title: str
  episode_id: int
  opening_crawl: str
  director: str
  producer: str
  release_date: str = Field(..., description="Formato YYYY-MM-DD")
  characters: List[str]