# MEOWS = 3 #// keep it in caps to indicate it's a constant 

# for _ in range(MEOWS):
#     print("Meow!")

#////////////////////////////////////////////////////////////////////////////////
# class Cat:
#     MEOWS = 3
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("Meow!")

# cat = Cat()
# cat.meow()
# # The above code defines a class Cat with a constant MEOWS and a method meow    


##////////////////////////////////////////////////////////////////////////////////
# def meow(n: int):
#     for _ in range(n):
#         print("Meow!")
        
# number : int = int(input("Number: "))
# meow(number)


#////////////////////////////////////////////////////////////////////////////////
def meow(n: int) -> str:
    return "Meow!\n" * n
        
number : int = int(input("Number: "))
meows: str = meow(number)  # This line is incorrect; it should not assign the result of
print(meows, end='')  # Print the result without adding an extra newline
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    
