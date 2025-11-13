from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()
engine = create_engine("sqlite:///students.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship("Course", secondary=student_course, back_populates="students")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship("Student", secondary=student_course, back_populates="courses")


def seed_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = SessionLocal()

    courses = [
        Course(title="Math"),
        Course(title="Physics"),
        Course(title="Biology"),
        Course(title="Alcology"),
        Course(title="History")
    ]
    session.add_all(courses)

    students = [Student(name=f"Student_{i}") for i in range(1, 21)]
    session.add_all(students)
    session.commit()

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))

    session.commit()
    session.close()
