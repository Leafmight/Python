from mypackage.classes.course import Course

class DataSheet:
    def __init__(self, lstCourses):
        self.lstCourses = lstCourses
    
    def __repr__(self): 
       return 'Datasheet(%r)' % (self.lstCourses)     
  
    def __str__(self):
        return '{lst}'.format(lst=self.lstCourses)

    def get_grades_as_list(self):
        lst_grade = []
        for course in self.lstCourses:
            lst_grade.append(course.grade)
        return lst_grade


if __name__ == "__main__":
    print("hello in datasheet")