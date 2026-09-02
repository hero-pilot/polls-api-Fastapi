import os
from fastapi import FastAPI, Request
from redis.asyncio import Redis
from contextlib import asynccontextmanager
 


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = Redis.from_url("redis://localhost:6379", decode_responses=True)
    yield
    await app.state.redis.close()

 
app = FastAPI(title="poll", lifespan=lifespan)
 
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


async def get_redis(request: Request) -> Redis:
    return request.app.state.redi