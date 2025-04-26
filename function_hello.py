def hello():
    print("Hello, " + name + "!")
    
# This is a simple function that takes a name as input and prints a greeting message.   
def hello_to(to):
    print("Hello, " + to + "!")

name = input("Enter your name: ")
hello()

print(name)

hello_to(name)