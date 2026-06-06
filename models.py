from pydantic import BaseModel
from datetime import datetime

class Actor(BaseModel):
    first_name : str
    last_name : str
    last_update : datetime