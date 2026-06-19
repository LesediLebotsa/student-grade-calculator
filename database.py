import sqlite3
import os
from calculations import calculate_grade

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
DB_PATH = os.path.join(
    BASE_DIR,
    "student.db"
)
def get_connection():
    return sqlite3.connect (DB_PATH)

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
         DELETE FROM students
         WHERE student_no = ?
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

def create_weightings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weightings (
        assessment TEXT PRIMARY KEY,
        weight REAL
        )
    """)
    conn.commit()
    conn.close()

def seed_weighting():
    conn = get_connection()
    cursor = conn.cursor()

    defaults = [
        ("Quiz", 10),
        ("Project", 20),
        ("Exam", 50),
        ("Practical", 20)
    ]
    for assessment, weight in defaults:
        cursor.execute("""
            INSERT OR IGNORE INTO weightings
            VALUES (?, ?)
        """, (assessment, weight))
    conn.commit()
    conn.close()

def get_weightings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT assessment, weight
        FROM weightings
    """)

    rows = cursor.fetchall()
    conn.close()

    return {
        assessment: weight
        for assessment, weight in rows
    }

def update_weighting(assessment,weight):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE weightings
        SET weight = ?
        WHERE assessment = ?
    """, (
        weight,
        assessment
    ))

    conn.commit()
    conn.close()
    
def recalculate_all_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM students
    """)

    students = cursor.fetchall()

    weights = get_weightings()

    for student in students:

        student_no = student[0]

        quiz = student[4]
        project = student[5]
        exam = student[6]
        practical = student[7]

        new_grade = (
            quiz * (weights["Quiz"] / 100) +
            project * (weights["Project"] / 100) +
            exam * (weights["Exam"] / 100) +
            practical * (weights["Practical"] / 100)
        )

        cursor.execute("""
            UPDATE students
            SET overall_grade = ?
            WHERE student_no = ?
        """, (round(new_grade, 2), student_no))

    conn.commit()
    conn.close()
