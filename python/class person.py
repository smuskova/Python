class Person:
    def __init__(self,name,family,age,nationality):
        self.fname=name
        self.lname=family
        self.Age=age
        self.Nationality=nationality
    def print_info(self):
        print(self.fname, self.lname, self.Nationality)
person1=Person('ivan', 'ivanov', 23, 'Bulgaria')
person1.print_info()
