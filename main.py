from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Seller
from schemas import Seller, SellerCreate
from database import SessionLocal, engine
from typing import List

# Создаем таблицы в БД
Seller.metadata.create_all(bind=engine)

app = FastAPI()


# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Получить всех продавцов
@app.get("/sellers/", response_model=List[Seller])
def get_all_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).all()
    return sellers


# 2. Получить продавца по ID
@app.get("/sellers/{seller_id}/", response_model=Seller)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller


# 3. Обновить продавца по ID
@app.put("/sellers/{seller_id}/update/", response_model=Seller)
def update_seller(seller_id: int, seller_data: SellerCreate, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")

    # Обновляем поля
    seller.name = seller_data.name
    seller.email = seller_data.email
    seller.phone = seller_data.phone

    db.commit()
    db.refresh(seller)
    return seller