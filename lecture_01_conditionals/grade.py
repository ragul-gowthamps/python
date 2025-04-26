def main():
    score = int(input("Enter score: "))
    
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score < 90:
       print("B")    
    elif score >= 70 and score < 80:
        print("C")    
    elif score >= 60 and score < 70:
        print("D")  
    else:
        print("F")   
    
main()

#improving by eliminating the keyword "and"
def main1():
    score = int(input("Enter score: "))
    
    if 90 <= score <= 100:
        print("A")
    elif 80 <= score < 90:
       print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    else:
        print("F")
    
main()

    
#improving using a try and except block to handle invalid inputs
# and using a while loop to keep asking for input until a valid score is entered.
def main2():
    while True:
        try:
            score = int(input("Enter score (0 to 100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Invalid input! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter an integer.")
    if 90 <= score :
        print("A")
    elif 80 <= score :
       print("B")
    elif 70 <= score :
        print("C")
    elif 60 <= score :
        print("D")
    else:
        print("F")

main2()