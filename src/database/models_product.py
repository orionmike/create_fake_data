
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import BaseModel


class Product(BaseModel):

    __tablename__ = 'product'

    name: Mapped[str]
    slug: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('category_product.id', ondelete="CASCADE"))
    price: Mapped[str]
    description: Mapped[str]
    is_published: Mapped[bool]


class CategoryProduct(BaseModel):

    __tablename__ = 'category_product'

    name: Mapped[str]
    slug: Mapped[str]
    description: Mapped[str]
    is_published: Mapped[bool]
