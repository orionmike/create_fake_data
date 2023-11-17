import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import BaseModel


class User(BaseModel):

    __tablename__ = 'user'

    uuid_user: Mapped[str] = mapped_column(unique=True, default=uuid.uuid4)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    address: Mapped[str]

    is_active: Mapped[bool]
