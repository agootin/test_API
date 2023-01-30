from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Person(Model):

    __tablename__ = 'person'

    person_id = Column(Integer, primary_key=True)
    person_name = Column(String)


class Movie(Model):

    __tablename__ = 'movie'

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
