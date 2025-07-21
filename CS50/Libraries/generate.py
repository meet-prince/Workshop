#-------------------------------------------------------------------------
# Using import and random.
# import random

# coin = random.choice(["heads","tails"])

# print(coin)

# 'import random' exrtract all the function that random have so, we use from to get some specific function from random.
#------------------------------------------------------------------------------

# So when you want to just use for choice randomly so you don't need to use random.choice(seq) we could directly use choice.()
# using "from random import choice"

# from random import choice

# coin = choice(["heads","tails"])
# print(coin)


#-----------------------------------------------------------------------------

#Using "random.randint(a,b)"

# import random
# number = random.randint(1,10)
# print(number)

#---------------------------------------------------------------------------
# Using "random.shuffle(x)"
        
import random

cards = ["jack",'queen',"king"]
random.shuffle(cards)
for card in cards:
    print(card)


#-----------------------------------------------------






