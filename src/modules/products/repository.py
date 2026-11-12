from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.products.models import ProductModel


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, product_id: int) -> ProductModel | None:
        return await self.session.get(ProductModel, product_id)

    async def get_all(self) -> Sequence[ProductModel] | None:
        result = await self.session.scalars(select(ProductModel))
        return result.all()

    async def create(self, product: dict) -> ProductModel:
        product = ProductModel(**product)
        self.session.add(product)
        await self.session.flush()
        return product

    async def update(self, product: ProductModel, updated_data: dict) -> ProductModel | None:
        for key, value in updated_data.items():
            setattr(product, key, value)

        await self.session.flush()
        return product

    async def delete(self, product: ProductModel) -> None:
        await self.session.delete(product)
        await self.session.flush()