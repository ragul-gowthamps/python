def main():
    name = input("Enter your name: ")
    hello(name)
    print(hello(name))
    
    
def hello(to="World"):
    return f"Hello, {to}!"

if __name__ == "__main__":
    main()
    # The following line is for testing purposes only
    # This will print "Hello, World!" if run directly
