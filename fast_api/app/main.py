from fastapi import FastAPI

app = FastAPI()
COUNT = 0

@app.get("/")
async def root():
    return {"message": "testing okay"}

@app.get("/count")
async def test():
    global COUNT
    COUNT += 1
    return {"message": f"Count is {COUNT}"}


