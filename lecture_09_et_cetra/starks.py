# students= [
#     {"name": "John", "house": "Stark"},
#     {"name": "Arya", "house": "Stark"},
# ]

# starks = [
#     student ["name"] for student in students if student["house"] == "Stark"]

# for stark  in sorted(starks):
#     print(stark)


# #//////////////////////////////////////////////////////
# students = [
#     {"name": "John", "house": "Stark"},
#     {"name": "Arya", "house": "Stark"},
# ]


# def is_stark(student):
#     return student["house"] == "Stark"


# starks = filter(is_stark, students)

# for stark in sorted(starks, key=lambda s: s["name"]):
#     print(stark["name"])


#//////////////////////////////////////////////////////

# students = ["John", "arya","sansa"]

# for i in range(len(students)):
#     print(f"{i+1}. {students[i]}")  


#//////////////////////////////////////////////////////
students = ["John", "arya","sansa"]

for i, student in  enumerate(students):
    print(f"{i+1}. {student}")  