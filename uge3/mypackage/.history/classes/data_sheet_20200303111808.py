from mypackage.classes.course import Course

class DataSheet:
    def __init__(self, courses):
        self.courses = courses
    
    def __repr__(self): 
       return 'Datasheet(%r)' % (self.courses)     
  
    def __str__(self):
        return '{lst}'.format(lst=self.courses)

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades


if __name__ == "__main__":
    print("hello in datasheet")