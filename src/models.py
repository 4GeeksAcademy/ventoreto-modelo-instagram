from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    posts: Mapped[list["Post"]] = relationship('Post', back_populates='user')
    comments: Mapped[list['Comment']] = relationship(
        'Comment', back_populates='user')
    likes: Mapped[list['Like']] = relationship('Like', back_populates='user')


class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    img_urg: Mapped[str] = mapped_column(String(250))
    caption: Mapped[str] = mapped_column(String(30))

    user: Mapped["User"] = relationship('User', back_populates='posts')
    comments: Mapped[list['Comment']] = relationship(
        'Comment', back_populates='post')
    likes: Mapped[list['Like']] = relationship('Like', back_populates='post')
    media: Mapped[list['Media']] = relationship('Media', back_populates='post')


class Comment(db.Model):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    user: Mapped['User'] = relationship('User', back_populates='comments')
    post: Mapped['Post'] = relationship('Post', back_populates='comments')


class Like(db.Model):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    user: Mapped['User'] = relationship('User', back_populates='likes')
    post: Mapped['Post'] = relationship('Post', back_populates='likes')


class Media(db.Model):
    __tablename__ = 'media'

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    post_id: Mapped[int] = mapped_column(
        ForeignKey('posts.id'), nullable=False)

    post: Mapped["Post"] = relationship("Post", back_populates="media")
