from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from domain.dto.stock_dto import StockCreateDto, StockUpdateDto

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sector = Column(String)

    def __init__(self, name: str, sector: str):
        self.name = name
        self.sector = sector

    @classmethod
    def from_create_dto(cls, dto: StockCreateDto):
        return cls(dto.name, dto.sector)

    def update_from_dto(self, dto: StockUpdateDto):
        if dto.name is not None:
            self.name = dto.name
        if dto.sector is not None:
            self.sector = dto.sector
