class Student:
    def __init__(self, name, course, univer):
        self.name = name
        self.course = course
        self.univer = univer

    def info(self):
        return f"{self.name.title()} {self.univer} universitetining {self.course}-kurs talabasi"

    def set_course(self, course):
        self.course = course

    def set_univer(self, univer):
        self.univer = univer


student1 = Student("Javlon", 4, "TATU")
student2 = Student("Yashnar", 3, "SamDu")

print(student1.info())
print(student2.info())

student1.set_univer("SamDu")
student2.set_course(4)

print(student1.info())
print(student2.info())
