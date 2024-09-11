
from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase): #Base class that all models will inherit
    pass


db = SQLAlchemy(model_class=Base)



class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True) #Auto incrementing pk
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    director_id: Mapped[int] = mapped_column(db.ForeignKey("directors.id"))


    director: Mapped["Director"] = db.relationship(back_populates="movies")


class Director(Base):
    __tablename__ = 'directors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)

    movies: Mapped[List["Movie"]] = db.relationship(back_populates="director")