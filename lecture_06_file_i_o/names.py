# names = []
# for _ in range(3):
#     names.append(input("Enter a name: "))
    
    
# print("The names you entered are:")
# for name in sorted(names):
#     print(f"hello,",name)

# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# # name = input("Enter a name: ")

# file = open ("lecture_06_file_i_o/names.text", "a")
# file.write(name + "\n")
# file.close()

# #xxxxxxxxxxxxxx
# # if we use WITH statement, we don't need to close the file explicitly.

# name = input("Enter a name: ")

# with open ("lecture_06_file_i_o/names.text", "a") as file:
#     file.write(name + "\n")

# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# # to read the file, we can use the readlines() method to read all lines at once.

# with open ("lecture_06_file_i_o/names.text", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print ("hello,",line.strip())

# ##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# # # to make it more elegant, we can use a list comprehension to read the lines and strip them at the same time.
# with open ("lecture_06_file_i_o/names.text", "r") as file:
#     for line in file:
#         print ("hello,",line.strip())
