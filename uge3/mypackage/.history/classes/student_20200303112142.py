from mypackage.classes.data_sheet import DataSheet
import sys

class Student():
    def __init__(self, name, gender, datasheet, img_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.img_url = img_url
    
    def __repr__(self): 
       return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.datasheet, self.img_url)     
  
    def __str__(self):
        return '{name}, {gender}, {datasheet}, {img_url}'.format(name=self.name, gender=self.gender, datasheet=self.datasheet, img_url=self.img_url),

    def get_avg_grade(self):
        return sum(self.datasheet.get_grades_as_list)/len(self.datasheet.get_grades_as_list)

if __name__ == "__main__":
    print("hello in student")