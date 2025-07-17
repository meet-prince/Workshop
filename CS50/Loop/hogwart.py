# About "List" ---> List is a set of multiple values 

# students = ["Harmione", "Harry", "Ron", "Draco"]
# This is a list of lenght 3.

# print(students[0])
# print(students[1])
# print(students[2])
# Instead of Typing manually for the list of students, Use for loop.

#---------------------------------------------------------------------
#i = 0

#.......................................
# for i in range(len(students)):
#     print(students[i])
#.....................................
# while i < len(students):
#     print(students[i])
#     i += 1
#.....................................
# The following code is little bit messy but it's a simplest version of upper codes. 
# for student in students:
#     print(student)

#.......................................

#-------------------------------------------------                      
# Printing with rank.
# i = 0 
# for i in range(len(students)):
#     print(i + 1,students[i])


#------------------------------------------------------
# Using Dictionary ----> dict - A dictionary is sort of 2 dimensional it associated with something to something else.

# house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# This one is not very good code what if students number will extrem.
# This will get messy quickly.

# students = {"Hermione": "Gryffindor",
#             "Harry": "Gryffindor",
#             "Ron": "Gryffindor",
#             "Draco": "Slytherin"}
# The upper code is a dictionary.
#.........................................
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
# The upper codes will give you their respective house names.

#....................................
# What'll happen if we swap the name with house then what it will execute?

# print(students["Gryffindor"])
# print(students["Gryffindor"])
# print(students["Gryffindor"])
# print(students["Slytherin"])

# It will show error.
#................................................


# for student in students:
#  # It will print only key.
#     print(student)

#------------------------------------------
# Now the following codes will print key and other things too called "value".
# I used sep="" which used to put any thing between two different printing values

# for student in students:
#     print(student, students[student], sep=" - ") 

#-------------------------------------------------------------
# What if we have more data to implement?
# I want to associated more thingh with students?

students =[
    {"name": "Harmione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Rusell Terrier"},
    {"name":"Draco", "house":"Gryffindor", "patronus": None}
]

# This is a list of dictionaries.
# This is a dictionary with same key but different values.

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" - ")









