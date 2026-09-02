from main import app, get_redis
from fastapi import status, Depends, APIRouter
from redis.asyncio import Redis
from app.models import PollRequest, PollResponse


router = APIRouter(
    prefix="/api",
    tags=["polls"]
)


@router.post("/polls", status_code= status.HTTP_201_CREATED)
async def create_poll(poll: PollRequest, redis: Redis = Depends(get_redis)):
    new_poll = poll.create_poll()
    redis.set(name=f"poll:{new_poll.id}" , value=new_poll)
    return {"detail": "Poll created successfully", "poll_id": new_poll.id}



app.include_router(router)