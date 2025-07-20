#        *
#       **
#      ***
#     ****
#    *****
#   ******
# Right Angled Triangle (Mirrored).

#----------------------------------------------

# p = int(input("what's p? "))

# i = 1
# j = p 
# while i <= p:
#     while j >= 1:
#         print(" " * j, "*" * i)
#         break
#     j -= 1
#     i += 1
    
# It's giving the desire output.

#---------------------------------------------------------------------------------------------

# Now, Create a function that could give this same output.

def main():
    while True:
        p = int(input("What's p? "))
        if p > 0:
            pattern(p)

            break

def pattern(p):
    i = 1
    j = p
    while i <= p:

        while j >= 0:
            print(" " * j, "*" * i) 
            break
        i += 1
        j -= 1

main()

# DONE

#-------------------------------------------------------------------------------------




