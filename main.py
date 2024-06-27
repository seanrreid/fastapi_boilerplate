import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from config import settings
from db import get_session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Root Route"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
