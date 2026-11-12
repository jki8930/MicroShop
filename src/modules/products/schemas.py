from decimal import Decimal
from pydantic import BaseModel, Field

class Base(BaseModel):
    model_config = {"from_attributes": True}

class ProductSchema(Base):
    id: int
    title: str
    description: str | None
    price: Decimal
    stock_quantity: int

class CreateProductSchema(Base):
    title: str = Field(min_length=1, max_length=50)
    description: str | None = None
    price: Decimal = Field(gt=0, decimal_places=2)
    stock_quantity: int = Field(default=0, ge=0)

class UpdateProductSchema(Base):
    title: str | None = None
    description: str | None = None
    price: Decimal | None = None
    stock_quantity: int | None = None

