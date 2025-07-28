# import cowsay
# import sys

# if len(sys.argv) == 2:
#     print(cowsay.cow(sys.argv[1]))
    # print(cowsay.trex("hello", sys.argv[1]))
# print("❤️  "*10," 💔 "*5)
from random import randint
while True:
    try:
        m = randint(1,100)

        a = int(input("N = "))
        print(a)
        break
    except ValueError:
        print("Invalid Input")
    