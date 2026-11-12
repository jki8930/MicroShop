from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import db_helper
from src.modules.products.repository import ProductRepository
from src.modules.products.service import ProductService

SessionDep = Annotated[AsyncSession, Depends(db_helper.session_getter)]

async def get_product_repository(session: SessionDep) -> ProductRepository:
    return ProductRepository(session)

ProductRepositoryDep = Annotated[ProductRepository, Depends(get_product_repository)]

async def get_product_service(repo: ProductRepositoryDep) -> ProductService:
    return ProductService(repo)

ProductServiceDep = Annotated[ProductService, Depends(get_product_service)]