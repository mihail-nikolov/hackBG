from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    result = Column(Integer)
    points = Column(Integer)

    def __str__(self):
        return "{} - {}, {}".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///players.db")
Base.metadata.create_all(engine)
