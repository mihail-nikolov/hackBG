from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "{} - {}, {}".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movies = relationship("Movie", backref="projections")
    movie_type = Column(String)
    movie_date = Column(String)
    movie_time = Column(String)

    def __str__(self):
        return "{} - m_id:{}; type:{}; {} {}".format(self.id, self.movie_id, self.movie_type, self.movie_date, self.movie_time)

    def __repr__(self):
        return self.__str__()


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    projections = relationship("Projection", backref="reservations")
    row = Column(Integer)
    col = Column(Integer)

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
