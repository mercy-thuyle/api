from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run 

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=[],
    max_age=60,
)

@app.get("/")
async def root():
    return {"message": "Successed => This is message from api."}

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port="8000")