from mypackage.classes.data_sheet import DataSheet
import sys

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name 
        self.gender = gender
        self.data_sheet = DataSheet(data_sheet.courses)
        self.image_url = image_url
    
    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def get_avg_grade(self):
        return sum(self.data_sheet.get_grades_as_list)/len(self.data_sheet.get_grades_as_list)

if __name__ == "__main__":
    print("hello in student")