from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: int

products: List[Product] = []

@app.get("/")
def get_root():
    return {"message": "Welcome to the world of FastAPI"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.get("/product")
def all_product():
    return products

@app.put("/product/{prod_id}")
def update_product(prod_id: int, updated_prod: Product):
    for index, product in enumerate(products):
        if product.id == prod_id:
            products[index] = updated_prod
            return updated_prod
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/product/{prod_id}")
def delete_product(prod_id: int):
    for index, product in enumerate(products):
        if product.id == prod_id:
            return products.pop(index)
    raise HTTPException(status_code=404, detail="Product not found")
