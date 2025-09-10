from fastapi import FastAPI

app = FastAPI(title="FastAPI Actions Demo")


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"status": "ok"}
