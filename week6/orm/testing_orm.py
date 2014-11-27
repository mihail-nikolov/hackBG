from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

# A class that maps to a table, inherits from Base
Base = declarative_base()


# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    #To print id and name in the console, not OBJ

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="grades")


engine = create_engine("sqlite:///university.db")
# will create all tables
#Base.metadata.create_all(engine)

"""
class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True)
    name = Column(String)`
    num_spec = Column(Integer)
    num_stud = Column(Integer)
"""

#engine1 = create_engine("sqlite:///faculty.db")

Base.metadata.create_all(engine)
#Base.metadata.create_all(engine1)


session = Session(bind=engine)

session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])

session.commit()

session.add(Student(name="Misho", age=23))
session.commit()

# SELECT * FROM student;
all_students = session.query(Student).all()
# list of Student objects
print(all_students)
rado = session.query(Student).filter(Student.name == "Rado").all()
print(rado)

tw_thr = session.query(Student).filter(Student.age == 23).all()
print(tw_thr)


rado = session.query(Student).filter(Student.name == "Rado").one()
rado.grades = [Grade(value=4), Grade(value=5), Grade(value=3)]
session.commit()

ivo = session.query(Student).filter(Student.name == "Ivo").one()
ivo.grades.append(Grade(value=6))
session.commit()


avg_grades = session.query((Grade.value)).filter(Grade.student_id == ivo.id).one()
print(avg_grades)
