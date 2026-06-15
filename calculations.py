def calculate_grade(quiz, project, exam, practical):
    if None in (quiz, project, exam, practical):
        return None

    overall = (
        quiz * 0.10 +
        project * 0.20 +
        exam * 0.50 +
        practical * 0.20
    )

    return round(overall, 2)

def get_grade_status(grade):
    if grade is None:
        return "Cannot Calculate"

    if grade >= 75:
        return "Distinction"

    elif grade >= 50:
        return "Pass"

    else:
        return "Fail"