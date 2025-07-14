name = input("What's your name? ")
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Harmione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")

#The upper code is checking four people of same house so we could combie thos with use of keyword or.
# if name == "Harry" or name == "Harmione" or name == "Ron":
#     print("Gryffindor")

# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who")

#---------------------------------------------------------

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Harmione":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who")

#-------------------------------------------------------------------------

#Lighting the upper code by all same house person tighting them into one single line.
match name:
    case "Harry" | "Harmione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")

#-------------------------------------------------------------

