# print("Meow")
# print("Meow")
# print("Meow")
#-----------------------------------------------------
# i = 0
# while i < 3:
#     print("meow")
    # i = i + 1
    # i += 1
    # "i += 2" this one also worked.


#What if i = 3.5
#-----------------------------------------------------
# Using For Loop
#for allows to itrate over following items.

# for i in [0, 1, 2]:
#     print("meow")  
# at exterem level you can't write 0 to 999...
#So, use a built in function called range(x) it will give you range of values like [0, 1, 2, ....., x - 1]

#------------------------------------------------------
#using range()

# for i in range(3):
    #range(3) wil give ---> [0, 1, 2] , instead of typing manually.
    # print("meow")  
#-----------------------------------------------------------------
#Notice that defining i but we will never using that again so we could improve this code. 
#Using _ (Underscore) instead of i
# for _ in range(3):
#     print("meow")

#------------------------------------------------------------------
# Instead of 'for' or 'while'
# print("meow" * 3) -----> meowmeowmeow

# print("meow\n" * 3)
#upper code's output is like :-
# meow
# meow
# meow
#           <----- but we will get extra one balnk line


#-----------------------------------------------------------------------
# Using end="" to not get that extra balnk line
#end="" it does that after executing certain code at the end it will print the stuffs inside the double quotes.
# for better understanding of 'end="good bye"' use it
# if you try to execute 'print("meow\n" * 3, end="good bye")' it will give the following output
# meow
# meow
# meow
# good bye

# print("meow\n" * 3, end="")
# upper code will print
# meow
# meow
# meow
# The upper codes in the block is not suitable so, this is a way to do but not good for users.

#--------------------------------------------------------------------------------------------------------------
# n = int(input("What's n? "))
# for i in range(n):
#     print("Meow")
# i = 0   
# while i < n:
#     print("meow")
#     i += 1
# The upper code is right but what if user will provide negative integers?
# So, Improved version is like following
# if n >= 0:
#     i = 0
#     while i < n:
#         print("meow")
#         i +=1
# else:
#     print("Error")

# The upper code is right but not that good, what if user will type negative number it will show "error" but instead of showing error why not asking same question tha "what's n? "


#------------------------------------------------------------


# while True:
#     print("meow")

# It'll print 'meow' for infinite times coz while True is always True.
#------------------------------------------------------
# It will ask question again and agian if user will provide negative number again and agian after.He/She realies the mistake and enter posetive integer then the while True loop will break otherwise it6 will countinue
# Using break and countinue

# while True:
#     n = int(input("What's n? "))
    # if n < 0:
    #     continue
    # else:
    #     break
    # The upper one is right too but not improved version like following.    
    # if n > 0:
    #     break


# for _ in range(n):
#     print("meow")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating a function

# VERY IMPORTANT CODES TO GET A BRIEF KNOWLEDGE ABOUT "FUNCTION".

def main(): #this one is the main function
    number = get_number()
    meow(number)

def meow(n): # This one is for How many times to print 'meow'
    # print("meow\n" * 3, end = "")
    for _ in range(n):
        print("meow")

def get_number(): # This one is for getting the number of times to print 'meow' from User.
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n # It will return the value of 'n' to get_number(n)
     
main()

#----------------------------------------------------------------------------------------------------------------



