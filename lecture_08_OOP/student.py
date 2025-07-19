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
# #adding patronus and charm method
# class Student:
#     def __init__(self,name, house, patronus):
#         if not name:
#             raise ValueError("Name cannot be empty")
#         house_lower = house.lower()
#         if house_lower not in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
    
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     def charm(self):
#         match self.patronus:
#             case "stag":
#                 return "Expecto Patronum stag!"
#             case "otter":
#                 return "Expecto Patronum otter!"
#             case "doe":
#                 return "Expecto Patronum doe!"
#             case _:
#                 return "Expecto Patronum unknown!"

# def main():
#     student = get_student()
#     print(student)
#     print(student.charm())  
#     # print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     # student = Student(name, house, patronus)
#     return Student(name, house, patronus)



# if __name__ == "__main__":
#     main()


# ///////////////////////////////////////////////////////

class Student:
    def __init__(self,name, house):
        self.name = name
        self.house = house
            
    def __str__(self):
        return f"{self.name} from {self.house}"



    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name   
    #getter
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self, house):
        house_lower = house.lower()
        if house_lower not in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin","stark"]:
            raise ValueError("Invalid house")
        self._house = house
        
        
def main():
    student = get_student()
    
    print(student)
    
   

def get_student():
    name = input("Name: ")
    house = input("House: ")
    
   
    return Student(name, house)



if __name__ == "__main__":
    main()
