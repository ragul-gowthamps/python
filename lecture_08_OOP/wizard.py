class Wizard:
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    def __init__(self,name, house):
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        



wizard = Wizard("Gandalf")
student = Student("Harry Potter", "Gryffindor")
professor = Professor("Albus Dumbledore", "Transfiguration")
print(f"Wizard: {wizard.name}")
print(f"Student: {student.name}, House: {student.house}")   
print(f"Professor: {professor.name}, Subject: {professor.subject}")