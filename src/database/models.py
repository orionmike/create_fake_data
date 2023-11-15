from datetime import datetime
from typing import Annotated, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow())]
updated_at = Annotated[
    datetime,
    mapped_column(
        default=datetime.utcnow(),
        onupdate=datetime.utcnow()
    )]


class User(Base):

    __tablename__ = 'user'

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    address: Mapped[str]

    is_active: Mapped[bool]

    datetime_create: Mapped[created_at]
    datetime_update: Mapped[updated_at]


class Product(Base):

    __tablename__ = 'product'

    id: Mapped[intpk]
    name: Mapped[str]
    category: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete="CASCADE"))
    price: Mapped[str]
    is_published: Mapped[bool]
    datetime_create: Mapped[created_at]
    datetime_update: Mapped[updated_at]


class CategoryProduct(Base):

    __tablename__ = 'category'

    id: Mapped[intpk]
    name: Mapped[str]
    is_published: Mapped[bool]
    datetime_create: Mapped[created_at]
    datetime_update: Mapped[updated_at]
