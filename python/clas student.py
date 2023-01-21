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
person1=Person('ivan', 'ivanov', 23, 'Bulgaria')
person1.print_info()
student1=Student('TU', '2021')
student1.print_info2()
