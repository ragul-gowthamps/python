# students=["Hermione","Harry","Ron","Draco"]
# houses=["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

# this is a dictionary
# a dictionary is a collection of key-value pairs
# a dictionary is a mutable data type
# a dictionary is unordered, changeable and indexed
students = {"Hermione": "Gryffindor",
           "Harry": "Gryffindor",
           "Ron": "Gryffindor",
           "Draco": "Slytherin"}

def main():
    print(students) # to print the whole dictionary
    print(students["Hermione"]) # to print the value of the key "Hermione"
    print(students["Harry"]) # to print the value of the key "Harry"
main()

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def main1():
    for student in students:
        print(student) # to print the keys of the dictionary
main1()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def main2():    
    for student in students:    
        print(student,students[student], sep=":") # to print the keys and values of the dictionary
main2()

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
def main3():
    new_students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
        ]
    print(new_students)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    for student in new_students:
        print(student["name"], student["house"], student["patronus"], sep="-")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

main3()    
