 from fastapi import FastAPI
 
 app = FastAPI()

@app.get("/")
async def root():
    return{ "message": "hello testing okay"}

if __name__ == "__main__":
    main()
