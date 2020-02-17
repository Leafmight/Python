from mypackage.classes import course

class DataSheet():
    def __init__(self, courses):
        self.courses = []
        for course in courses:
            new_course = course(course.name, course.classroom, course.teacher, course.ETCS, course.grade)
            self.courses.append(new_course)