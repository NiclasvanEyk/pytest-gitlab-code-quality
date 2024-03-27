import warnings

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class UserPosts(Base):
    comment: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    author: Mapped["User"] = relationship(back_populates="post_links")
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    post: Mapped["Post"] = relationship(back_populates="author_links")

    __tablename__: str = "user_post"


class User(Base):
    name: Mapped[str]
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    posts: Mapped[list["Post"]] = relationship(
        back_populates="authors", default_factory=list, secondary="user_post"
    )
    post_links: Mapped[list[UserPosts]] = relationship(
        back_populates="author", default_factory=list
    )

    __tablename__: str = "user"


class Post(Base):
    title: Mapped[str]
    body: Mapped[str]
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    authors: Mapped[list[User]] = relationship(
        back_populates="posts", default_factory=list
    )
    author_links: Mapped[list[UserPosts]] = relationship(
        back_populates="post", default_factory=list, secondary="user_post"
    )

    __tablename__: str = "post"


def foo():
    warnings.warn("Something will be removed!")
    warnings.warn("Test!")

    user = User(name="Test")
    post = Post(title="How to run Pytest", body="...")

    return "foo"
