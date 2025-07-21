# x = int(input("What's x? "))

# print(f"x is {x}")
# x = cat
# ValueError: invalid literal for int() with base 10: 'cat'
#---------------------------------------------------------------------------

# Using keyword try & except to handle the ValueError.
# So, instead of showing error it will show 
# What's x? cat
# x is not an integer.

# try:
#     x = int(input("What's x? "))

#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer.")


#-----------------------------------------------------------------------------





# try:
#     x = int(input("What's x? "))
    
# except ValueError:
#     print("x is not an integer.")

# print(f"x is {x}")

# NameError: name 'x' is not defined




#-------------------------------------------------------------------------

# Using else:

# try:
#     x = int(input("What's x? "))
    
# except ValueError:
#     print("x is not an integer.")
# else:
#     print(f"x is {x}")


#-----------------------------------------------------------------------------

# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer.")
    

# print(f"x is {x}")


#-----------------------------------------------------------------------------
# Creating a function.

# def main():
#     x = get_int()
#     print(f"x is {x}.")



# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")
#         else:
#             #break
#             # instead of break use return because its doing two things one is it break the loop and return the value.
#             return x
# main()


#-----------------------------------------
# More refined version.

# def main():
#     x = get_int()
#     print(f"x is {x}.")



# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#             # x = int(input("What's x? "))

#         except ValueError:
#             print("x is not an integer.")
# main()

#---------------------------------------------------------
# Using "pass"

def main():
    x = get_int()
    print(f"x is {x}.")



def get_int():
    while True:
        try:
            return int(input("What's x? "))
            # x = int(input("What's x? "))

        except ValueError:
            pass
main()

# May be it worse or good depend on you.




#----------------------------------------------------------------------------








