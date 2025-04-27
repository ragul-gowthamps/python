def main():
    while True:
        n = int(input("Enter a number : "))
        if n < 0:
            continue
        else:
            break
    
    for _ in range(n):
        print("meow3")
        
main()

def main1():
    while True:
        n = int(input("Enter a number : "))
        if n > 0:
            break
    
    for _ in range(n):
        print("meow3")
        
main1()

def main3():
    n = get_number()
    meow(n)
    
def meow(n):
    for _ in range(n):
        print("meow3")

def get_number():
    while True:
        n = int(input("Enter a number : "))
        if n > 0:
            return n
        else:
            print("Please enter a positive number.")

main3()