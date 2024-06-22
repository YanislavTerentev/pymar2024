def students():
    students_data = [
        "Johnny, group_1,7,8,8,9,10",
        "Steve, group_2,2,5,7,4,8",
        "Alex, group_3,7,8,8,9,8",
        "Tim, group_3,2,4,5,0,10",
        "Jack, group_1,5,9,2,3,8",
        "Bettie, group_2,1,5,8,9,4",
        "Veronica, group_2,7,0,8,9,8",
        "Emili, group_1,3,8,8,1,8",
        "Jessie, group_1,2,2,6,9,10"
    ]

    try:
        with open('students.txt', 'w', encoding='utf-8') as file:
            for student in students_data:
                file.write(student + '\n')

        with open('students.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            students_in_group = {}
            groups_marks = {}
            for line in lines:
                students_in_line = line.strip().split(",")
                students_group = students_in_line[1]
                students_marks = list(map(int, students_in_line[2:]))

                if students_group not in students_in_group:
                    students_in_group[students_group] = 0
                    groups_marks[students_group] = 0

                students_in_group[students_group] += 1
                groups_marks[students_group] = students_marks

        with open('students.txt', 'a', encoding='utf-8') as file:
            file.write(f"\nTotal students: {len(lines)}\n")
            file.write(f"\nStudents in groups: {students_in_group}\n")

    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except (IndexError, ValueError):
        print("Index Error")


students()
