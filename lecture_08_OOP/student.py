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
    
    
    

def main():
    student = get_student()
    if student["name"].lower() == "padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
      