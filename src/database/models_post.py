
from typing import Annotated, List, Optional, Set

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from database.models import BaseModel


class CategoryPost(BaseModel):

    __tablename__ = 'category_post'

    name: Mapped[str]
    slug: Mapped[str]
    description: Mapped[str]
    is_published: Mapped[bool]


class AssociationPostTag(Base):
    __tablename__ = "association_post_tag"

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)
    # extra_data: Mapped[Optional[str]]

    tag: Mapped["Tag"] = relationship(back_populates="post_list")
    post: Mapped["Post"] = relationship(back_populates="tag_list")


class Tag(BaseModel):

    __tablename__ = 'tag'

    name: Mapped[str]
    slug: Mapped[str]
    description: Mapped[str]

    # manyy to many
    posts: Mapped[List['Post']] = relationship(secondary='association_post_tag', back_populates="tags")
    post_list: Mapped[List["AssociationPostTag"]] = relationship(back_populates="tag")

    is_published: Mapped[bool]


class Post(BaseModel):

    __tablename__ = 'post'

    name: Mapped[str]
    slug: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('category_post.id', ondelete="CASCADE"))

    # manyy to many
    tags: Mapped[List['Tag']] = relationship(secondary='association_post_tag', back_populates="posts")
    tag_list: Mapped[List["AssociationPostTag"]] = relationship(back_populates="post")

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"))

    prewiew_text: Mapped[str]
    full_text: Mapped[str]

    is_published: Mapped[bool]
