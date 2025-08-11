from pydantic import BaseModel
from typing import List, Optional

class Intake(BaseModel):
    age_band: Optional[str] = None
    falls: str
    bathing: str
    stairs: str
    carer_strain: str
    hazards: List[str] = []
