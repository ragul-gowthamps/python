students = [
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Luna Lovegood", "house": "Ravenclaw"},
    {"name": "Cedric Diggory", "house": "Hufflepuff"},
]

# # usage of list
# houses =[]
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#         print(f"Added {student['house']} to houses.")

# for house in sorted(houses):
#     print(house)


#////////////////////////////////////////////
 
# usage of set

houses = set() 
for student in students:
    houses.add(student["house"])
    
for house in sorted(houses):
    print(house)

