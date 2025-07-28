# THIS IS A PROTOTYPE FORTHE ORIGINAL GAME "Game-3".
# In this error could occur and stop the game.
# I've improved this game in another file. 

import random
import cowsay

m = random.randint(1,100)

print("Levels  Available In This Game. ")
print("Choose 1 for Easy - (10 Chances)")
print("Choose 2 for Easy - (5 Chances)")
print("Choose 3 for Easy - (3 Chances)")
while True:
    L = int(input("Choose a level:  "))

    if L == 1:
        print("You have total 10 lives:"," ❤️ "*10)
        i = 1
    

        while True:
            while i <= 10:
                n = int(input("Guess a number Between 1 to 100: "))
    
                if i != 10:
                    if  n > m:
                        print(f"{n} is greater than the number.")
                        print("❤️  " * (10-i),"🤍 "*i)
                        i += 1  

            
                    elif n < m:
                        print(f"{n} is smaller than the number.")
                        print("❤️  " * (10-i),"🤍 "*i)
                        i += 1
            
                    elif n == m:
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 " *i)
                    print("You Lost Chances Overed.")
                    print(f"{m} is the number.")
                    break
            break
    elif L == 2:
        print("You have total 5 lives:"," ❤️ "*5)
        i = 1
    

        while True:
            while i <= 6:
                n = int(input("Guess a number Between 1 to 100: "))
    
                if i != 5:
                    if  n > m:
                        print(f"{n} is greater than the number.")
                        print("❤️  " * (5-i),"🤍 "*i)
                        i += 1  

            
                    elif n < m:
                        print(f"{n} is smaller than the number.")
                        print("❤️  " * (5-i),"🤍 "*i)
                        i += 1
            
                    elif n == m:
                        
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 "*i)
                    print("You Lost Chances Overed.")
                    print(f"{m} is the number.")
                    break
            break
    elif L==3:
        i = 1
    
        print("You have total 3 lives:"," ❤️ "*L)
    

        while True:
            while i <= 3:
                n = int(input("Guess a number Between 1 to 100: "))
                
    
                if i != 3:
                    if  n > m:
                        print(f"{n} is greater than the number.")
                        print("❤️  " * (3-i),"🤍 "*i)
                        i += 1  

            
                    elif n < m:
                        print(f"{n} is smaller than the number.")
                        print("❤️  " * (3-i),"🤍 "*i)
                        i += 1
            
                    elif n == m:
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 "*i)
                    print("You Lost Chances Overed.")
                    print(f"{m} is the number.")
                    break
             
            break
        
    else:
        cowsay.cow("Invalid Level")

          
        
        
    
