x = float(input("What's x? "))
y = float(input("What's y? "))
z = float(input("What's z? "))
if x > y:
    print(z) if z > x else print(x)
if y > x:
    print(z) if z > y else print(y)


#-----------------------------------------------------
# Doing same problem using only 'if'-


# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = float(input("What's z? "))
# if z > y and x > z:
#     print(x)
# if z < y and x > y:
#     print(x)

# if z > x and y > z:
#     print(y)
# if z < x and y > x:
#     print(y)

# if y > x and z > y:
#     print(z)
# if y < x and z > x:
#     print(z)


#---------------------------------------------------------------------

