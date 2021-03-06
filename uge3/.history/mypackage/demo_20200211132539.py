from mypackage.classes.course import Course
from mypackage.classes.data_sheet import DataSheet
from mypackage.classes.student import Student
import sys
import random
import platform
import csv

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

def write_list_to_file(output_file, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        
        output_writer = csv.writer(output_file)
        for line in lst:
            output_writer.writerow(line)


def generate_students(n):
    lst_students = ()
    for i in range(n):
        lst_courses = [Course(rc(lst_course_names), rc(lst_classrooms), rc(lst_teachers), rc(lst_ETCS), rc(lst_grades)) for i in range(3)]
        new_dataSheet = DataSheet(lst_courses)
        lst_students.append(Student(rc(lst_names), rc(lst_gender), new_dataSheet, rc(lst_imgurl)))
     
    write_list_to_file('students.csv', lst_students)

def read_csv():
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open('students.csv', newline=newline) as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list

def print_students():
    for student in read_csv():
        print(student)

if __name__ == "__main__":
    print("Hello in demo")
    generate_students(2)
    print(print_students())