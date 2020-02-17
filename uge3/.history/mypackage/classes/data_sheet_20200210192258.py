from mypackage.classes.course import Course

class DataSheet():
    def __init__(self, courses):
        self.courses = []
        for course in courses:
            new_course = Course(course.name, course.classroom, course.teacher, course.ETCS, course.grade)
            self.courses.append(new_course)
    
    def get_grades_as_list(self):
        lstgrade = []
        for course in courses:
            lstgrade.append(course.grade)


if __name__ == "__main__":
    print("hello in datasheet")