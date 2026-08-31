from pydantic import BaseModel, Field
import uuid
from typing import List
from datetime import datetime, timezone


class PollRequest(BaseModel):
    title: str = Field(min_length=5 , max_length=50)
    options: List[str] = Field(min_length=2 , max_length=5)
    expires_at: datetime | None = Field(default=None)



    def create_poll(self) -> PollResponse:
            choices= [
                ChoiceResponse(
                    description= i,
                    label= index +1
                ) for index , i in enumerate(self.options)
            ]
            if self.expires_at is not None and self.expires_at < datetime.now(timezone.utc):
                 raise ValueError("expiration date must be in the future.")
            return PollResponse(options=choices, expires_at=self.expires_at, title=self.title)

class PollResponse(PollRequest):
    id : uuid.UUID = Field(default_factory= uuid.uuid4())
    options: List[ChoiceResponse]
    created_at : datetime = Field(default_factory= datetime.now(timezone.utc))






class ChoiceRequest(BaseModel):
    description : str = Field(min_length=1 , max_length=100)

class ChoiceResponse(ChoiceRequest):
    id : uuid.UUID = Field(default_factory= uuid.uuid4())
    label : int = Field(ge=1, le=5)
