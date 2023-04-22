from pydantic import BaseModel


class StockBase(BaseModel):
    name: str
    sector: str


class StockCreateDto(StockBase):
    pass


class StockUpdateDto(StockBase):
    pass


class StockDto(StockBase):
    id: int

    class Config:
        orm_mode = True
