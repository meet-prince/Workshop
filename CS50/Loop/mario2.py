# def main():
#     get_height(3)



# def get_height(h):
#     while True:
#         h = int(input("What's height? "))
#         w = int(input("What's width? "))

#         if h >= 0 and w >= 0:
            
#             for i in range(w):
                
#                 for j in range(h):
#                     print("# " )
#             break
            




# main()

#Completly wrong!!!!!!!!!!!!!!! 

#-----------------------------------


# def main():
#     get_height(3)



# def get_height(h):
#     while True:
#         h = int(input("What's height? "))
#         w = int(input("What's width? "))

#         if h >= 0 and w >= 0:
            
#             for i in range(h):
                
#                 print("#  " * w )
#             break
            




# main()

#--------------------------------------------------------------------------------------

# Simple method to do this problemo.

# h = int(input("What's h? "))
# w = int(input("what's w? "))

# for i in range(h):
#     print("# " * w)

# But what if user will give negative integers.

#----------------------------------------------------------------

# New and Improved.

# h = int(input("What's h? "))
# w = int(input("what's w? "))
# if h >= 0 and w >= 0:
#     for i in range(h):
#         print("#  " * w)
# else:
#     print("Error")

# This one is good but instead of showing 'Error', why not ask to user the same question again!

#---------------------------------------------------------

# New and Improved.

# while True:
#     h = int(input("What's h? "))
#     w = int(input("what's w? "))
#     if h >= 0 and w >= 0:
#         for i in range(h):
#             print("#  " * w)
#         break

#------------------------------------------------------------------------------------------------------------------------

# Doing same stuff but using function.
# Keep getting Errors...


# def main():

#     get_height(1)
#     get_width(1)
#     square(1,1)

# def get_height(h):
#     while True:
#         h = int(input("What's h? "))
#         if h >= 0:
#             break

# def get_width(w):
#     while True:
#         w = int(input("What's w? "))
#         if w >= 0:
#             break

# def square(h,w):
#     for i in range(h):
#         print("#  " * w)

# main()

#------------------------------------------------------------------------------------------------------
# Instead of making three functions which are very messy to control create only 2 one is main() and another is blocks().

# def main():
#     blocks(1)

# def blocks(h,w):
#         h = int(input("What's h? "))
#         w = int(input("What's w? "))
#         if h >= 0 and w >= 0:
#             for i in range(h):
#                 print("#  " * w)

#             break

# main()

# The upper code will ask both h and w again if user will entered negative integer for h or w or both but that is not convinece.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------


# def main():
#     blocks(1,1)

# def blocks(h,w):
#     while True:
#         h = int(input("What's h? "))
#         if h >= 0:
#             while True:
#                 w = int(input("What's w? "))
#                 if w >= 0:
#                     for i in range(h):
#                         print("#  " * w)
        
                    
#                     break
#             break
# main()

# This code will check firstly weather thefirst value that is h is correct or not if it doesn't correct then the code will ask the same question again and if true then it will ask next question if second input is not correct then it will only ask second question only wheather the given input for second variable w is not correct if it is correct then it will print the desire output.

#-----------------------------------------------------------------------------------------------------------------------------------------

# In the following codes what I did is, I've created only one function and taking input from user via main funtion in which the varible h and w are now in these codes the h and w are not now any more local varible these became global variable.

def blocks(h,w):

    for i in range(h):
        print("#  " * w)
        


while True:
    h = int(input("What's h? "))
    if h > 0:
        while True:
            w = int(input("What's w? "))
            if w > 0:
                blocks(h,w)
                break
        break
#------------------------------------------------------------------------------------------------------------------------------------------------------



