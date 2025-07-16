# x = float(input("What's x? "))

# if x >= 1 and x <= 100:
#     print("Yes")
# else:
#     print("No")

#---------------------
# Writting the code without using 'AND'.
# x = float(input("What's x? "))
# if 1 <= x <= 100:
#     print("Yes")
# else:
#     print("No")

#----------------------------------
# Mergingin if and else in one line

# x = float(input("What's x? "))
# print("Yes") if 1 <= x <= 100 else print("No")

#---------------------------------------------------
# Creating Function and using Boolean

def main():
    x = float(input("What's x? "))
    if true(x):
        print("Yes")
    else:
        print("No")

def true(numb):
   return True if 1 <= numb <= 100 else False
main()