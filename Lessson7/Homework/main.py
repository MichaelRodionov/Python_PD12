import functions as f


def main():
    """
    Main function
    """
    students_file = "students.json"
    professions_file = "professions.json"
    students_list = f.load_students(students_file)
    pk_max = len(students_list) + 1

    pk_input = int(input("Enter the number of student: "))
    if pk_max > pk_input:
        name, skills = f.get_student_by_pk(students_list, pk_input)

        print(f'Student {name}\nKnows {skills}')

        title_input = input(f'Enter a profession to estimate student {name}: ').capitalize()
        titles, titles_list = f.load_professions(professions_file)
        if title_input in titles_list:
            title_set = f.get_profession_by_title(titles, title_input)
            skills_set = set(skills.split(", "))
            fitness_check = f.check_fitness(title_set, skills_set)
            print(f'Fitness {fitness_check["fit_percent"]}%\n'
                  f'{name} knows {", ".join(fitness_check["has"])}\n'
                  f'{name} dont know {", ".join(fitness_check["lacks"])}')
        else:
            print("We dont have such title")
    else:
        print("No such student")
        quit()


if __name__ == "__main__":
    main()
