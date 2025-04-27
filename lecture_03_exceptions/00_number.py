# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code that handles the exception
# else:
#     # Code that runs if no exceptions are raised
# finally:
#     # Code that always runs, regardless of what happened before

def main():
    while True:
        try :
           x = int(input("Enter 0th number: "))
        except ValueError:
            print("That's not a valid number!") # This will catch the ValueError if the input is not an integer
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")# This will catch the KeyboardInterrupt if the user presses Ctrl+C
        else:
           print(f"You entered: {x}")
           break # If no exception occurs, break out of the loop
        finally:
            print("program0 ended .") # This will always run, regardless of whether an exception occurred
main()

#xxxxxxxxxxxxxxxxxxxxxxxxx
def main1():
    while True:
        try :
           x = int(input("Enter 1st number: "))
           break
        except ValueError:
            print("That's not a valid number!") # This will catch the ValueError if the input is not an integer
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")# This will catch the KeyboardInterrupt if the user presses Ctrl+C
        
        #if you have used a break statement in the try block, you don't need to use it in the else block.
        # The else block is executed only if the try block does not raise an exception.
        else:
           print(f"You entered: {x}")
           break # If no exception occurs, break out of the loop
        finally:
            print("i will execute anyway as I am inside finally .") # This will always run, regardless of whether an exception occurred
main1()



#xxxxxxxxxxxxxxxxxxxxxxxxx
#breaking the loop using break under else block
def main2():
    x =get_int()
    print(f"You entered: {x}") 
    
def get_int():
    while True:
        try:
            x = int(input("Enter 2nd number: "))
        except ValueError:
            print("That's not a valid number!") # This will catch the ValueError if the input is not an integer
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")# This will catch the KeyboardInterrupt if the user presses Ctrl+C
        else:
            print("No exception occurred.")
            break
        finally:
            print("i will execute anyway") # This will always run, regardless of whether an exception occurred
            
    return x # Return the value if no exception occurs

main2()


#xxxxxxxxxxxxxxxxxxxxxxxx
#breaking the loop using return under else block
def main3():
    x =get_int()
    print(f"You entered: {x}")
   
   
    
def get_int():
    while True:
        try:
            x = int(input("Enter 3rd number: "))
        except ValueError:
            print("That's not a valid number!") # This will catch the ValueError if the input is not an integer
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")# This will catch the KeyboardInterrupt if the user presses Ctrl+C
        else:
            return x # Return the value if no exception occurs
        finally:
            print("i will execute anyway and am using return  under else which will break the loop") # This will always run, regardless of whether an exception occurred
            
    
main3()

#xxxxxxxxxxxxxxxxxxxxxxxxx
#breaking the loop using return under try block

def main4():
    x =get_int()
    print(f"You entered: {x}")

def get_int():
    while True:
        try:
            return int(input("Enter 4th number: "))
        except ValueError:
            print("That's not a valid number!")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
        finally:    
            print("i will execute anyway and am using return under try which will break the loop")
main4()


#xxxxxxxxxxxxxxxxxxxxxxxxx

#using pass statement in finally block


def main5():
    x =get_int()
    print(f"You entered: {x}")

def get_int():
    while True:
        try :
            return int(input("Enter 5th number: "))
        except ValueError:
            pass # This will catch the ValueError if the input is not an integer
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")# This will catch the KeyboardInterrupt if the user presses Ctrl+C
main5()


#xxxxxxxxxxxxxxxxxxxxxxxxx
def main6():
    x =get_int("enter 6th number: ")
    print(f"You entered: {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass
main6()