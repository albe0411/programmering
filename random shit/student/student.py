class Student:
    def __init__(self, f_name : str, l_name : str, year : int, grades : list[int]):
        self.f_name = f_name
        self.l_name = l_name
        self.year = year
        self.grades = grades

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    def average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def __str__(self):
        return f"{self.f_name} {self.l_name} from year {self.year} have these grades {self.grades}, and the average grade is {self.average_grade()}"

class Classroom:
    def __init__(self, name : str, students : list):
        self.name = name
        self.students = students

    def best_student(self):
        for i in range(len(self.students)):
            if i == 0 or self.students[i].average_grade() > curent_best_student.average_grade():
                curent_best_student = self.students[i]
        return f"the best student is {curent_best_student}"

    def __str__(self):
        students = ""
        for i in range(len(self.students)):
            students += f"{self.students[i].__str__()}. "
        return str(students)

valid_grades = [1, 2, 3, 4, 5]
student1 = Student("Thomas", "Béldi", 2023, [4, 1, 2, 3])
student2 = Student("Alvin", "Berglund", 2023, [5, 5, 3, 5])
classroom1 = Classroom("TE23", [student1, student2])

print(classroom1.best_student())

while True:
    try:
        user_input = input("what do you want to do, see who is the best student or see student info (bs, si): ")
        match user_input:
            case "bs":
                print(classroom1.best_student())
            case "si":
                user_input = input("what do you want to do, see student info of all students or access one students info (all, one): ")
                match user_input:
                    case "all":
                        print(classroom1)
                    case "one":
                        while True:
                            try:
                                user_input = input("what do you want to do, add a grade or see student info or exit (ag, si, ex): ")
                                if user_input == "ex":
                                    break
                                else:
                                    student_number = input("wich student would you like to access(1, 2, ...): ")
                                    match user_input:
                                        case "ag":
                                            while True:
                                                new_grade = int(input("what grade do you want to add?: "))
                                                if new_grade in valid_grades:
                                                    exec(f"student{student_number}.add_grade(new_grade)")
                                                    print("new grade added")
                                                    break
                                                else:
                                                    print("not a valid grade")
                                        case "si":
                                            print(eval(f"student{student_number}"))
                                        case _:
                                            print("invalid input")
                            except NameError:
                                print("invalid student number")
                    case _:
                        print("invalid input")
            case _:
                print("invalid input")
                    
    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break