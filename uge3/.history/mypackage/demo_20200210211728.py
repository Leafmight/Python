from mypackage.classes.course import Course
from mypackage.classes.data_sheet import DataSheet
from mypackage.classes.student import Student
import sys
import random

print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))
lst_teachers = ["Elon Musk", "Steve Jobs", "Bill Gates"]
lst_names = ["Kurt Wonnegut", "Hans Hansen", "Peter Petersen", "Pia Nielsen", "Mette Wonnegut"]
lst_gender = ["Male", "Female"]
lst_grades = [0, 2, 4, 7, 10, 12]
lst_classroom = [1.01, 1.62, 3.12]
lst_ETCS = [10, 20, 30]
lst_imgurl = []

def generate_students(n):
    return n

def get_teachers():
        return lst_teachers[int(random.random()]

    # lst_courses = [Course(name, classroom, teacher, ETCS, grade) for range(0, n)]

if __name__ == "__main__":
    print("Hello in demo")
    print(get_teachers())