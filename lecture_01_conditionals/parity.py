# This is a simple script that checks if a number is even or odd.

def main():
    # This is a simple script that prints "Hello, World!" to the console.
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
main()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main1():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
main1()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main2():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main2()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main3():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main3()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxx