 from fastapi import FastAPI
 
 app = FastAPI()
COUNT=0
@app.get("/")
async def root():
    return{ "message": "hello testing okay"}

@app.get("/count")
async def test():
    COUNT= COUNT++
    return {"mesage": f"Count is  {COUNT}"}
    
# if __name__ == "__main__":
#     main()
