# script to find out the house of a student in hogwarts
name = input("Enter the name of the student: ")
def main():
    if name =="Harry":
        print("gryffindor")
    elif name == "Hermione":
        print("gryffindor")
    elif name == "Ron":
        print("gryffindor")
    elif name == "Draco":
        print("slytherin")
    else:
        print("not a member of hogwarts")

main()

#xxxxxxx
def main1():

    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("gryffindor")
    elif name == "Draco":
        print("slytherin")
    else:
        print("not a member of hogwarts")

main1()

#xxxxxxxxxxxxxxx


match name:
    case "Harry":
        print("gryffindor")
    case "Hermione":
        print("gryffindor")
    case "Ron":
        print("gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("not a member of hogwarts")
#xxxxxxxxxxxx
match name:
    case "Harry" |"Hermione" | "Ron":
        print("gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("not a member of hogwarts")



