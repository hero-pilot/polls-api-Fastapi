from main import app
from fastapi import status
from app.models import PollRequest, PollResponse


@app.post("/polls", status_code= status.HTTP_201_CREATED)
def create_poll(poll: PollRequest):
    new_poll = poll.create_poll()
    return {"detail": "Poll created successfully", "poll_id": new_poll.id}


