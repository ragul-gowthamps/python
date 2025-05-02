from calculator import square

def main():
    test_square()
    print("test_done")
    test_square_1()
    print("test_1_done")

def test_square():
    if square(2) != 4:
        print("Test failed!")
    if square(-3) != 9:
        print("Test failed!") 
    else:
        print("Test passed!")

#using try and except with assert statement
def test_square_1():
    
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(-3) == 9
    except AssertionError:
        print("3 squared was not 9")
    
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
        
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

    
    
if __name__ == "__main__":
    main()
    