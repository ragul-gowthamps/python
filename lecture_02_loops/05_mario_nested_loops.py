def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")      
main()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main1():
    print_column(3)


def print_column(height):
    print("$\n" * height, end="")
main1()      


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def main2():
    print_row(4)

def print_row(width):
    print("?" * width)

main2()


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main3():
    def print_square(size):
        #for each row in the square
        for i in range(size):
            #for each column in the square
            for j in range(size):
                print("#", end="")
            print()
    print_square(3)
main3()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def main4():
    
    def print_square(size):
        for i in range(size):
            print("/" * size)
    print_square(3)    
main4()