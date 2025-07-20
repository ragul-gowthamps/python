# def main():
#     yell("this is a test")
    
# def yell(phrase):
#     print(phrase.upper())
    
# if __name__ =="__main__":
#     main()



# #//////////////////////////////////////////////////////////////////////////
# def main():
#     yell("this", "is", "a test")

# def yell(*phrases):
#     uppercased = []
#     for word in phrases:
#         uppercased.append(word.upper())
#     print(*uppercased)
    
# if __name__ =="__main__":
#     main()

#//////////////////////////////////////////////////////////////////////////
# def main():
#     yell("this", "is", "a test")

# def yell(*phrases):
#     uppercased = map(str.upper, phrases)
#     print(*uppercased)
    
# if __name__ =="__main__":
#     main()





#/#//////////////////////////////////////////////////////////////////////////
##list comprehension
def main():
    yell("this", "is", "a test")    

def yell(*phrases):
    uppercased = [word.upper() for word in phrases]
    print(*uppercased)
    
    
if __name__ =="__main__":
    main()