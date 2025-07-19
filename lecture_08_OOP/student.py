# name = input("Name:")
# house = input("House:")
# print(f"{name} from {house}")

# //////////////////////////////////////
# def main():
#     student = get_student()
#     if student[0] =="padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
    
# # def get_name():
# #     return input("Name: ")

# # def get_house():
# #     return input("House: ")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()
    
    # ///////////////////

# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student={}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()
      
    # ///////////////////
    
    
    

# def main():
#     student = get_student()
#     if student["name"].lower() == "padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

# ///////////////////      

# class Student:
#     ...
    
    
    
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

#//////////////////////////////////////////////////

class Student:
    def __init__(self,name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)
    # print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student



if __name__ == "__main__":
    main()
