import json


def load_students(students_json):
    """
    Get json file of students and return list of students
    """
    with open(students_json) as file:
        students = json.load(file)
        return students


def load_professions(professions):
    """
    Get json file of professions and return list of professions and dictionary of professions
    """
    professions_dict = {}
    professions_list = []
    with open(professions) as file:
        titles = json.load(file)
    for profession in titles:
        professions_dict[profession["title"]] = profession["skills"]
        professions_list.append(profession["title"])
    return professions_dict, professions_list


def get_student_by_pk(students, pk_input):
    """
    Return students name with skills by pk input
    """
    for student in students:
        if student["pk"] == pk_input:
            knowledge = ", ".join(student["skills"])
            full_name = student["full_name"]
            return full_name, knowledge


def get_profession_by_title(titles, title_input):
    """
    Return set of title skills by title input
    """
    return set(titles[title_input])


def check_fitness(title_set, skills_set):
    """
    Return dictionary with student fitness to title skills
    """
    has = list(skills_set.intersection(title_set))
    lacks = list(title_set.difference(skills_set))
    fit_percent = int(len(has) / len(title_set) * 100)
    fit_dict = {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent
    }
    return fit_dict
