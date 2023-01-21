class Person:
    def __init__(self,name,family,age,nationality):
        self.fname=name
        self.lname=family
        self.Age=age
        self.Nationality=nationality
    def print_info(self):
        print(self.fname, self.lname, self.Nationality)
class Student(Person):
    def __init__(self, university, yearofstudy):
        
        self.uni=university
        self.year=yearofstudy
    def print_info2(self):
        print(self.uni, self.year)
class Lecture(Person):
    def __init__(self,university, experience):
        
        self.uni=university
        self.xp=experience
    def print_info3(self):
        print(self.uni, self.xp)
person1=Person('ivan', 'ivanov', 23, 'Bulgaria')
person1.print_info()
student1=Student('TU', '2021')
student1.print_info2()
lecture1=Person('Ivan', 'Danailov', 40, 'Bulgaria')
lecture2=Lecture('TU', 5)
lecture1.print_info()
lecture2.print_info3()
