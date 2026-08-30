from pydantic import BaseModel, Field
import uuid
from typing import List
from datetime import datetime, timezone


class PollRequest(BaseModel):
    title: str = Field(min_length=5 , max_length=50)
    options: List[str]
    expires_at: datetime | None = Field(default=None)

class PollResponse(PollRequest):
    id : uuid.UUID = Field(default_factory= uuid.uuid4())
    options: List[ChoiceResponse]
    created_at : datetime = Field(default_factory= datetime.now(timezone.utc))
   




class ChoiceRequest(BaseModel):
    description : str = Field(min_length=1 , max_length=100)

class ChoiceResponse(ChoiceRequest):
    id : uuid.UUID = Field(default_factory= uuid.uuid4())
    label : int = Field(ge=1, le=5)
