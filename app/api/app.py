from main import app
from fastapi import status
from app.models import PollRequest, PollResponse


@app.post("/polls", status_code= status.HTTP_201_CREATED, response_model=PollResponse)
def create_poll(poll: PollRequest):
    return PollResponse(
        title= poll.title, 
        options= poll.options,
        expires_at= poll.expires_at
    )