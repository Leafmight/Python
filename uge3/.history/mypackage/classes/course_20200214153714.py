class Course:

    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name 
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    #def __repr__(self):
     #  return 'Course( %r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ETCS, self.grade)
    
    def __str__(self):
        return self.name + ", " + self.classroom + ", " + self.teacher + ", " + self.ETCS + ", " + self.grade

    