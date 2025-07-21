#---------------------------------------------------------------------------------
# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")

# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")


# print("hello, my name is",sys.argv[1])

#--------------------------------------------------------------------------------

# Using slice in list[starting index:where to stop]

# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# for arg in sys.argv[1:-1]:
#     print("hello, my name is",arg)

# print(len(sys.argv))


#------------------------------------------------------------------------------

# Packages - third party libraries.
#You and i can install and implement it on our code.
# Search "pypi.or"  for python packages.
# Like cowsay
#pip  (package manager) is a program taht comes with python that use to install package on to your own pc or cloud by just runnig a code.
#  This is the output ofthe following codes.
#  _____________
# | hello, Prince |
#   =============
#              \
#               \
#                 ^__^
#                 (oo)\_______
#                 (__)\       )\/\
#                     ||----w |
#                     ||     ||

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# This is called ACII arts.
#---------------------------------------------------------------------------------


import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])


#--------------------------------------------------------------------------------






