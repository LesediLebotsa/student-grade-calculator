from database import get_students

def total_students():
    return len(get_students())

def average_grade():
    students = get_students()

    grades = [
        student[8]
        for student in students
    ]

    return round(
        sum(grades) / len(grades),
        2
    )

def pass_rate():
    students = get_students()

    passed = [
        s
        for s in students
        if s[8] >= 50
    ]

    return round(
        len(passed) /
        len(students) * 100,
        2
    )

def distinction_rate():
    students = get_students()

    distinctions = [
        s
        for s in students
        if s[8] >= 75
    ]

    return round(
        len(distinctions) /
        len(students) * 100,
        2
    )

def top_student():
    students = get_students()

    return max(
        students,
        key=lambda student: student[8]
    )

def module_averages():
    students = get_students()

    modules = {}

    for student in students:
        module = student[3]
        grade = student[8]

        if module not in modules:
            modules[module] = []

        modules[module].append(
            grade
        )

    averages = {}

    for module, grades in modules.items():

        averages[module] = round(
            sum(grades) / len(grades),
            2
        )
    return averages

def best_module():
    averages = module_averages()

    return max(
        averages,
        key = averages.get
    )

def worst_module():
    averages = module_averages()

    return min(
        averages,
        key = averages.get
    )

def top_10_students():
    students = get_students()

    return sorted(
        students,
        key = lambda s: s[8],
        reverse = True
    )[:10]

def failure_rate():
    students = get_students()

    failed = [
        s
        for s in students
        if s[8] < 50
    ]
    return round(
        len(failed) /
        len(students) * 100,
        2
    )