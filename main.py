import os
from fastapi import FastAPI, Request
from redis.asyncio import Redis
from contextlib import asynccontextmanager
from dotenv import load_dotenv


load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = Redis.from_url(REDIS_URL, decode_responses=True)
    yield
    await app.state.redis.close()

 
app = FastAPI(title="poll", lifespan=lifespan)
 
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


async def get_redis(request: Request) -> Redis:
    return request.app.state.redi

