class Students:
    def __init__(self, first_name, last_name, grade, attendance):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.attendance = attendance

    def good_stu(self):
        if self.grade in "AB" and self.attendance >= 80:
            print("{} {} is a very good student".format(self.first_name, self.last_name))
        elif self.grade in "AB" and self.attendance  >= 40 < 80:
            print("{} {} is a very good student but attendance could be better".format(self.first_name, self.last_name))
        elif self.grade in "AB" and self.attendance < 40:
            print("{} {} is a very good student but attendance is very bad".format(self.first_name, self.last_name))
        elif self.grade in "CD" and self.attendance >= 80:
            print("{} {} is a good student ".format(self.first_name, self.last_name))
        elif self.grade in "CD" and self.attendance  >= 40 < 80:
            print("{} {} is a good student but attendance could be better".format(self.first_name, self.last_name))
        elif self.grade in "CD" and self.attendance < 40:
            print("{} {} is a good student but attendance is very bad".format(self.first_name, self.last_name))
        elif self.grade in "EF" and self.attendance >= 80:
            print("{} {} has a good attendance but grades are bad".format(self.first_name, self.last_name))
        elif self.grade in "EF" and self.attendance >= 40 < 80:
            print("{} {}'s grades are bad".format(self.first_name, self.last_name))
        elif self.grade in "EF" and self.attendance < 40:
            print("{} {}'s grades and attendance is bad".format(self.first_name, self.last_name))


    def __del__(self):
        print("{} {} was deleted from the system".format(self.first_name, self.last_name))

    def __str__(self):
        return "{} {} has {} grade and {}% attendance".format(self.first_name, self.last_name, self.grade, self.attendance)
            
       
        
        
