def validate_mark(mark, student_name, assessment):
    if mark == "":
        print(f"WARNING: {student_name} has a missing {assessment} mark.")
        return None

    try:
        mark = float(mark)

    except ValueError:
        print(f"WARNING: {student_name} has an invalid {assessment} mark.")
        return None

    if mark < 0 or mark > 100:
        print(f"WARNING: {student_name} has a {assessment} mark above 100.")
        return None

    return mark