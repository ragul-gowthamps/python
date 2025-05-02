import sys 

def main():
    try:
        print("Hello, my name is",sys.argv[0])
    except IndexError:
        print("Hello, my name is John Doe")
    
main()


def main1():
    #check for errors
    if len(sys.argv) < 2:
        print("too few arguments")
    elif len(sys.argv) > 2:
        print("too many arguments")
    # else:
    #     print("Hello, my name is", sys.argv[1])

main1()


print("main1 done")

def main2():

    #check for errors
    if len(sys.argv) < 2:
        sys.exit("too few arguments")
    # elif len(sys.argv) > 2:
    #     sys.exit("too many arguments")
        
main2()
print("main1 done")
print("Hello, my name is", sys.argv[1]) 


def main3():
    if len(sys.argv) < 2:
        sys.exit("too few arguments")
    for arg in sys.argv:
        print("Hello, my name is", arg)
main3()
print("main3 done")