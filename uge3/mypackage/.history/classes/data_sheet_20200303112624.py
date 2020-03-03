from mypackage.classes.course import Course

class DataSheet():
    def __init__(self, courses):
        self.courses = courses
      
    def __str__(self):
        return str(self.courses)
    
    def get_grades_as_list(self):
        lst_grade = []
        for course in self.courses:
            lst_grade.append(course.grade)
        return lst_grade


if __name__ == "__main__":
    print("hello in datasheet")