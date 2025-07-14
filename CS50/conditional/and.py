score = int(input("Score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score>= 70 and score <80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#------------------------------------------------------------------------------

#I following codes we just filliped the absolute score and student score
# if 90 <= score and 100 >= score:
#     print("Grade: A")
# elif 80 <= score and 90 > score:
#     print("Grade: B")
# elif 70 <= score and 80 > score:
#     print("Grade: C")
# elif 60 <= score and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#the upper codes worked as well.

#----------------------------------------------------------------------------------------------

#Now in following codes, instead of and we just put the score between the conditions. 
# if 90 <=  score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#yup, this one worked too(Without using 'and' keyword).

#------------------------------------------------------------
#make code mutually exclusive
# if score >= 90:
#     print("Grade: A")
# if score >= 80:
#     print("Grade: B")
# if score >= 70:
#     print("Grade: C")
# if score >= 60:
#     print("Grade: D")
#it will execute all grades.
#---------------------------------------------------------------

#For the following codes instead like upper codes i just make it more simple by using one conditional operator.
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")