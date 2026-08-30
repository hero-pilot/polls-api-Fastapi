
from fastapi import FastAPI
 
app = FastAPI(title="poll")
 
 
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
 
