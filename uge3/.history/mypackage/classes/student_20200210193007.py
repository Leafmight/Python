from mypackage.classes.data_sheet import DataSheet
import sys

print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name 
        self.gender = gender
        self.data_sheet = DataSheet(data_sheet.courses)
        self.image_url = image_url
    
    def get_avg_grade(self):
        return sum(self.data_sheet.get_grades_as_list)/len(self.data_sheet.get_grades_as_list)

if __name__ == "__main__":
    print("hello in student")