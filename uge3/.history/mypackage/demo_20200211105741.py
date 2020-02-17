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
lst_imgurl = []
def rl(lst):
    return random.choice(lst)
lst_courses = [Course(random.choice(lst_course_names), random.choice(lst_classrooms), random.choice(lst_teachers), random.choice(lst_ETCS), random.choice(lst_grades)) for i in range(10)]

def generate_students(n):
    lst_students = []

    return lst_students

def get_teachers():
        return random.choice(lst_teachers)

    # lst_courses = [Course(name, classroom, teacher, ETCS, grade) for range(0, n)]

if __name__ == "__main__":
    print("Hello in demo")
    print(get_teachers())
    print(lst_courses)