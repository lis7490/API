from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models import Seller
from schemas import SellerCreate, SellerResponse
from database import SessionLocal, engine

# Создаем таблицы в БД
Seller.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/sellers/", response_model=List[SellerResponse])
def get_all_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).all()
    return sellers


@app.get("/sellers/{seller_id}/", response_model=SellerResponse)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Seller with id {seller_id} not found"
        )
    return seller


@app.put("/sellers/{seller_id}/update/", response_model=SellerResponse)
def update_seller(
        seller_id: int,
        seller_data: SellerCreate,
        db: Session = Depends(get_db)
):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Seller with id {seller_id} not found"
        )

    seller.name = seller_data.name
    seller.email = seller_data.email
    seller.phone = seller_data.phone

    db.commit()
    db.refresh(seller)
    return seller