x= float(input("Enter first number: "))
y= float(input("Enter second number: "))


z=round(x+y)
print(f"{z:,}") # output with commas every third digit
print(f"{z:.2f}") # output with 2 decimal places


z1=round(x/y,2)
# print(f"{z1:}") 
# print(f"{z1:.2f}") # output with 2 decimal places
print(f"{z1:,.2f}") # output with 2 decimal places and commas every third digit

def main():
    x =int(input("whats x? "))
    print("x squared is", square(x))
    print("x squared is", square_1(x))
    print("x squared is", square_2(x))
    
def square(n):
    return n * n

def square_1(n):
    return n ** 2

def square_2(n):
    return pow(n, 2)

main()