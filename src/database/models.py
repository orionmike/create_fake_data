
from datetime import datetime
from typing import Annotated, Optional

from sqlalchemy.orm import mapped_column, Mapped
from database.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow())]
updated_at = Annotated[
    datetime,
    mapped_column(
        default=datetime.utcnow(),
        onupdate=datetime.utcnow()
    )]


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[intpk]
    datetime_create: Mapped[created_at]
    datetime_update: Mapped[updated_at]
