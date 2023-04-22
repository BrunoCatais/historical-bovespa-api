from fastapi import FastAPI

from adapters.controllers.stock_controller import router as stock_router
from adapters.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(stock_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
