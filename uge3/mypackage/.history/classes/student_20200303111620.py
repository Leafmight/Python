from mypackage.classes.data_sheet import DataSheet
import sys

class Student():
    def __init__(self, name, gender, datasheet):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
    
    def __repr__(self): 
       return 'Student(%r, %r, %r)' % (self.name, self.gender, self.datasheet)     
  
    def __str__(self):
        return '{name}, {gender}, {datasheet}'.format(name=self.name, gender=self.gender, datasheet=self.datasheet)

    def get_avg_grade(self):
        return sum(self.datasheet.get_grades_as_list)/len(self.data_sheet.get_grades_as_list)

if __name__ == "__main__":
    print("hello in student")