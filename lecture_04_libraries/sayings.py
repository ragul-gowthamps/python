def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!") 

if __name__ == "__main__":
    # This is the main entry point of the script
    # It will only run if this file is executed directly
    # and not if it is imported as a module in another script
    main()