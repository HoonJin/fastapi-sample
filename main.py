from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    result = {"hello": "world"}
    return result
