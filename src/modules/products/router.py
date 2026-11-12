from collections.abc import Sequence

from fastapi import APIRouter, status

from src.modules.products.schemas import ProductSchema, CreateProductSchema, UpdateProductSchema
from src.modules.products.dependencies import ProductServiceDep


router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/{id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def get_product(id: int, service: ProductServiceDep):
    return await service.get_by_id(id)

@router.get("/", response_model=Sequence[ProductSchema], status_code=status.HTTP_200_OK)
async def get_all_products(service: ProductServiceDep):
    return await service.get_all()

@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: CreateProductSchema, service: ProductServiceDep):
    return await service.create(product)

@router.patch("/{id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def update_product(id: int, product: UpdateProductSchema, service: ProductServiceDep):
    return await service.update(id, product)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int, service: ProductServiceDep):
    return await service.delete(id)