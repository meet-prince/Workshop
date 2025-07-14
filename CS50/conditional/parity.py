# x = int(input("What's x? "))
# if x % 2 ==0:
#     print("Even")
# else:
#     print("Odd")

#--------------------------------------------------
#I'm creating a function for this parity.
# def main():
#     x = int(input("What's x? "))
#     oddeven(x)

# def oddeven(numb):
#     if numb % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# main()
#-------------------------------------------------------

#Using Boolean That is 0/1 or True/False.
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")

    else:
        print("Odd")

# def is_even(numb):
#     if numb % 2 == 0:
#         return True
#     else:
#         return False
# def is_even(numb):
#     if numb % 2 == 0:
#         return 1
#     else:
#         return 0

#In the followiing codes I've combimned all 4 conditional line into one.
# def is_even(numb):
#     return 0 if numb % 2 != 0 else 1



#In the following codes numb % 2 gives remainder 0 the it will execute even else odd.
def is_even(numb):
    return numb % 2 == 0

main()
#-----------------------------------------------------

