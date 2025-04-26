# This is a simple function that takes a name as input and prints a greeting message.   

name = input("Enter your name: ")

print(name)


def hello():
    print("Hello, " + name + "!")

hello()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxx
def hello_to(to):
    print("Hello, " + to + "!")

hello_to(name)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxx
def hello_to_world(to="world"):
    print("Hello, " + to + "!")
    
hello_to_world()
hello_to_world(name)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxx



def main():
    new_name = input("Enter your new_name: ")
    new_hello(new_name)
      
 
def new_hello(new_parameter):
    print("Hello, " + new_parameter + "!")
    
main() 
#xxxxxxxxxxxxxxxxxxxxxxxxxxxx