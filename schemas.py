from pydantic import BaseModel, EmailStr

class SellerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class SellerCreate(SellerBase):
    pass

class SellerResponse(SellerBase):
    id: int

    class Config:
        orm_mode = True