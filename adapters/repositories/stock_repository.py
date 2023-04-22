from sqlalchemy.orm import Session

from domain.entities.stock import Stock as StockEntity


class StocksRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, stock: StockEntity) -> StockEntity:
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return stock

    def get(self, stock_id: int) -> StockEntity:
        return self.db.query(StockEntity).filter(StockEntity.id == stock_id).first()

    def save(self, stock: StockEntity) -> StockEntity:
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return stock

    def delete(self, stock_id: int) -> None:
        self.db.query(StockEntity).filter(StockEntity.id == stock_id).delete()
        self.db.commit()
