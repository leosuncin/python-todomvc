from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Greet(BaseModel):
    message: str


@app.get("/greeting")
def say_hi(name: str = "World") -> Greet:
    return Greet(message=f"Hello {name}")
