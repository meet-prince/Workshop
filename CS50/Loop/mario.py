# Creating three vertical blocks like in mario game 

#---------------------------------------------
# print("#\n" * 3, end="")
#----------------------------------------------
# for _ in range(3):
#     print("#")

#--------------------------------------------

# def main():
#     print_column(3)

# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * height, end="")

# main()

#-------------------------------------------------

# Printing four horizontral question marks like in mario game through which mario gets coins.

# def main():
#     print_row(4)

# def print_row(width):
#     print("?  " * width)

# main()


#------------------------------------------------------------
# Now I'm going to print a 3 by 3 square block represented by 0 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        
        #  print("0 " * size) #this one will also give same output.
        # The upper one is string multiplication trick.
        for j in range(size):
        
                print("# ", end="")
        
        
        print() # This one is for print new line by default whenever the upper code will exit the loop.

main()


#-----------------------------------------------------------------------------------






