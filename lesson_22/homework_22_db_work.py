from homework22_db_setup import SessionLocal, seed_database, Student, Course


def add_student(name: str, course_id: int):
    session = SessionLocal()

    course = session.get(Course, course_id)

    if not course:
        print(f"Course with ID {course_id} not found!")
        session.close()
        return

    student = Student(name=name)
    student.courses.append(course)

    session.add(student)
    session.commit()

    print(f"Added {name} to course {course.title}")

    session.close()


def update_student(student_id: int, new_name: str):
    session = SessionLocal()
    student = session.get(Student, student_id)

    if not student:
        print("Student not found!")
        session.close()
        return

    student.name = new_name
    session.commit()
    session.close()


def delete_student(student_id: int):
    session = SessionLocal()
    student = session.get(Student, student_id)

    if not student:
        print("Student not found!")
        session.close()
        return

    session.delete(student)
    session.commit()
    session.close()


def update_course(course_id: int, new_title: str):
    session = SessionLocal()
    course = session.get(Course, course_id)

    if not course:
        print("Course not found!")
        session.close()
        return

    course.title = new_title
    session.commit()
    session.close()


def delete_course(course_id: int):
    session = SessionLocal()
    course = session.get(Course, course_id)

    if not course:
        print("Course not found!")
        session.close()
        return

    session.delete(course)
    session.commit()
    session.close()


def students_in_course(course_id: int):
    session = SessionLocal()
    course = session.get(Course, course_id)

    if not course:
        session.close()
        return []

    result = list(course.students)
    session.close()
    return result


def courses_of_student(student_id: int):
    session = SessionLocal()
    student = session.get(Student, student_id)

    if not student:
        session.close()
        return []

    result = list(student.courses)
    session.close()
    return result


if __name__ == "__main__":
    seed_database()

    add_student("John Wick", 1)

    print("\nStudents in Math (course_id=1):")
    for s in students_in_course(1):
        print(" -", s.name)

    print("\nCourses of Student_1:")
    for c in courses_of_student(1):
        print(" -", c.title)
