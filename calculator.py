x= float(input("Enter first number: "))
y= float(input("Enter second number: "))


z=round(x+y)
print(f"{z:,}") # output with commas every third digit
print(f"{z:.2f}") # output with 2 decimal places


z1=round(x/y,2)
# print(f"{z1:}") 
# print(f"{z1:.2f}") # output with 2 decimal places
print(f"{z1:,.2f}") # output with 2 decimal places and commas every third digit