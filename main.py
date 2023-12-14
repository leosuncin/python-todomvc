from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Greet(BaseModel):
    message: str


@app.get("/greeting", response_model=Greet)
def say_hi(name: str = "World"):
    return {"message": f"Hello {name}"}
