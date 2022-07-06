import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    server_port = int(os.environ.get('PORT', '8000'))
    uvicorn.run("main:app", host="0.0.0.0", port=server_port, log_level="info")
