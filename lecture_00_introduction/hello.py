print("Hello, World!",end=" ") #usage of end in print function

"""
comments
""" #usage triple quote for multiline comments

name = input("What's your name?") #usage of input function


name = name.strip() # remove leading and trailing spaces

name = name.capitalize() # capitalize the first letter of the name

print(f"Hello, {name}!") #usage of f-string for string formatting


name = name.title() # capitalize the first letter of each word in the name
print("welcome", name, sep="???")  #usage of sep in print function

print("trying 'quotes'") #usage of quotes in strings

location = input("what's your current location?").strip().title() #usage of input,strip and title function
#
print(f"{location} is a great place to live!") #usage of f-string for string formatting
print("trying \"quotes\"") #usage of \ in strings
