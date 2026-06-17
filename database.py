import sqlite3

def get_connection():
    return sqlite3.connect ("student.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_no TEXT PRIMARY KEY,
            name TEXT,
            surname TEXT,
            module TEXT,
            quiz REAL,
            project REAL,
            exam REAL,
            practical REAL,
            overall_grade REAL
        )
    """)

    conn.commit()
    conn.close()

def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student["Student No"],
        student["Name"],
        student["Surname"],
        student["Module"],
        student["Quiz(10%)"],
        student["Project(20%)"],
        student["Final Exam(50%)"],
        student["Practical(20%)"],
        student["Overall Grade"]
    ))

    conn.commit()
    conn.close()

def delete_student(student_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        "DELETE FROM students"
        " WHERE student_no = ?
        """,
        (student_no,)
    )

    conn.commit()
    conn.close()

def student_exists(student_no):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_no FROM students WHERE student_no = ?",
        (student_no,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None

def get_student_by_number(student_no):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_no = ?
        """,
        (student_no,)
    )

    student = cursor.fetchone()

    conn.close()

    return student

def update_student(
        student_no,
        assessment,
        new_mark
):

    conn = get_connection()
    cursor = conn.cursor()

    column_map = {
        "Quiz(10%)": "quiz",
        "Project(20%)": "project",
        "Final Exam(50%)": "exam",
        "Practical(20%)": "practical"
    }

    column_name = column_map[assessment]

    cursor.execute(
        f"""
        UPDATE students
        SET {column_name} = ?
        WHERE student_no = ?
        """,
        (new_mark, student_no)
    )

    cursor.execute(
        """
        SELECT quiz,
               project,
               exam,
               practical
        FROM students
        WHERE student_no = ?
        """,
        (student_no,)
    )

    quiz, project, exam, practical = cursor.fetchone()

    overall_grade = (
        quiz * 0.10 +
        project * 0.20 +
        exam * 0.50 +
        practical * 0.20
    )

    cursor.execute(
        """
        UPDATE students
        SET overall_grade = ?
        WHERE student_no = ?
        """,
        (
            round(overall_grade, 2),
            student_no
        )
    )

    conn.commit()
    conn.close()

def get_students():
    conn = get_connection()
    cursor =conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    """)
    students = cursor.fetchall()

    conn.close()

    return students