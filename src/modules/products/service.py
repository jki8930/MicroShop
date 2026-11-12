from collections.abc import Sequence

from pydantic import TypeAdapter

from src.modules.products.exceptions import ProductNotFoundExc
from src.modules.products.schemas import CreateProductSchema, UpdateProductSchema
from src.modules.products.repository import ProductRepository
from src.modules.products.schemas import ProductSchema


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    async def get_by_id(self, product_id: int) -> ProductSchema:
        product_model = await self.repo.get_by_id(product_id)
        if not product_model:
            raise ProductNotFoundExc("Product not found")

        return ProductSchema.model_validate(product_model)

    async def get_all(self) -> Sequence[ProductSchema]:
        product_models = await self.repo.get_all()

        adapter = TypeAdapter(list[ProductSchema])
        return adapter.validate_python(product_models)

    async def create(self, create_product_data: CreateProductSchema) -> ProductSchema:
        product_model = await self.repo.create(create_product_data.model_dump())
        return ProductSchema.model_validate(product_model)

    async def update(self, product_id: int, update_product_data: UpdateProductSchema) -> ProductSchema:
        product_model = await self.repo.get_by_id(product_id)
        if not product_model:
            raise ProductNotFoundExc("Product not found")

        updated_product_model = await self.repo.update(product_model, update_product_data.model_dump(exclude_unset=True))
        return ProductSchema.model_validate(updated_product_model)

    async def delete(self, product_id: int) -> None:
        product_model = await self.repo.get_by_id(product_id)
        if not product_model:
            raise ProductNotFoundExc("Product not found")

        await self.repo.delete(product_model)