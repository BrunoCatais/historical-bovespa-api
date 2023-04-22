from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from adapters.database.db import SessionLocal
from adapters.repositories.stock_repository import StocksRepository
from domain.dto.stock_dto import StockCreateDto, StockUpdateDto
from domain.entities.stock import Stock

router = APIRouter()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/stocks")
async def create_stock(stock_create_dto: StockCreateDto, db: Session = Depends(get_db)):
    stocks_repository = StocksRepository(db)
    stock = Stock.from_create_dto(stock_create_dto)
    stocks_repository.create(stock)
    return stock


@router.get("/stocks/{stock_id}")
async def get_stock(stock_id: int, db: Session = Depends(get_db)):
    stocks_repository = StocksRepository(db)
    stock = stocks_repository.get(stock_id)
    return stock


@router.put("/stocks/{stock_id}")
async def update_stock(stock_id: int, stock_update_dto: StockUpdateDto, db: Session = Depends(get_db)):
    stocks_repository = StocksRepository(db)
    stock = stocks_repository.get(stock_id)
    stock.update_from_dto(stock_update_dto)
    stocks_repository.save(stock)
    return stock


@router.delete("/stocks/{stock_id}")
async def delete_stock(stock_id: int, db: Session = Depends(get_db)):
    stocks_repository = StocksRepository(db)
    stocks_repository.delete(stock_id)
    return {"message": "Stock deleted successfully"}
