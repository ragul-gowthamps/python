def main():
    students = ["Hermione", "Harry", "Ron"]
    
    print(students[0])
    print(students[1])
    print(students[2])
main()



#xxxxxxxx


def main1():
    students = ["Hermione", "Harry", "Ron"]
    
    for student in students:
        print(student)

main1()


#xxxxxxx


def main2():
    students = ["Hermione", "Harry", "Ron"]
    
    for i in range(len(students)):
        print(students[i])
main2()


#xxxxxxxxx 
# to print the list in reverse order

def main3():
    students = ["Hermione", "Harry", "Ron"]
    n = len(students)
    for n in range(n):
        print(n+1,students[n-1])
        n -= 1
main3()


