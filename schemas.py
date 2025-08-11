from pydantic import BaseModel

class SellerBase(BaseModel):
    name: str
    email: str
    phone: str

class SellerCreate(SellerBase):
    pass

class Seller(SellerBase):
    id: int

    class Config:
        orm_mode = True  # Для работы с SQLAlchemy моделями