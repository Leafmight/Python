from mypackage.classes.course import Course
from mypackage.classes.data_sheet import DataSheet
from mypackage.classes.student import Student
import sys
import random

print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))
lst_teachers = ["Elon Musk", "Steve Jobs", "Bill Gates"]
lst_names = ["Kurt Wonnegut", "Anne Hansen", "Peter Olsen", "Pia Nielsen", "Mette Pedersen"]
lst_course_names = ["Python", "JavaScript", "Java", "C++"]
lst_gender = ["Male", "Female"]
lst_grades = [0, 2, 4, 7, 10, 12]
lst_classrooms = [1.01, 1.62, 3.12]
lst_ETCS = [10, 20, 30]
lst_imgurl = ["img1", "img2", "img3"]

def rc(lst):
    return random.choice(lst)


def generate_students(n):
    lst_students = []
    i = 0
    while i < n:
        lst_courses = [Course(rc(lst_course_names), rc(lst_classrooms), rc(lst_teachers), rc(lst_ETCS), rc(lst_grades)) for i in range(10)]
        new_dataSheet = DataSheet(lst_courses)
        lst_students.append(Student(rc(lst_names), rc(lst_gender), new_dataSheet, rc(lst_imgurl)))

    return lst_students

def get_teachers():
        return random.choice(lst_teachers)

    # lst_courses = [Course(name, classroom, teacher, ETCS, grade) for range(0, n)]

if __name__ == "__main__":
    print("Hello in demo")
    print(get_teachers())
    for student in generate_students(6):
        print(student)
