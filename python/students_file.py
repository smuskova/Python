class Student:
    def __init__(this,student_id,name, language):
        this.student_id=student_id
        this.name=name
        this.language=language
    def gedID(this):
        return this.student_id
    def getName(this):
        return this.name
    def getLanguage(this):
        return this.language

def addStudent(student):
    with open('students.txt', 'a') as file:
        file.write(f"{student.getNmae()}, {student.getID()}, {student.getLanguage()}")

n=int(input("number of students: "))
print();

i=0
while(i<n):
    print(f"Student {i+1}:")
    name= input("Name:")
    student_id= input("ID:")
    language= input("Programing language:")
    print()
    student= Student(student_id, name,language)
    addStudent(student)
