
# Final Version of Game-2, Game-3 and Game-4.
# I just added functions and a feature through which if  user want to play again then he/she could no need to run code again!

#-------------------------------------------------------------------------------------------------------------------------
# Importing randint from random module.

from random import randint
#------------------------------------------------------------------------------------------------------------------------
# This block of code will ask to user that he/she want to play again or not! 

def again():
    
        try:

            print("Do you Want to play this game again?")
            print("Press 'Y' for yes or 'N' for No")
            c = input("Y/N: ").title().strip()
            if c == "Y":
                main()
                
        except ValueError:
            print("Invalid Input!")

#--------------------------------------------------------------------------------------------------------------------------
# This block will take ask for level.

def choose():
    while True:
        print("There are 3 Levels.")
        print("Press 1 for EASY - 7 Lives❤️")
        print("Press 2 for MODERATE - 5 Lives❤️")
        print("Press 3 for HARD - 3 Lives❤️")
        try:
            c = int(input("Choose a level: "))
            if c > 0 and c < 4:
                if c == 1:
                    print("You have Choosed Level 1.")

                    level(7)
                    break
                elif c == 2:
                    print("You have choosed Level 2.")
                    level(5)
                    break
                else:
                    print("You have choosed level 3.")
                    level(3)
                    break
            else:
                print("You Choosed Invalid Level.")
        except ValueError:
            print("It's not an integer.")

#------------------------------------------------------------------------------------------------------------------------
# This is like Kernel of any OS.
# It will ask for guessed integer from user. 

def level(x):
    m = randint(1,20)
    i = 1
    print("❤️  "*x, " <--- LifeMeter")
    if x == 7:
        
        while True:
            try:
                g = int(input("Guess a number between 1 to 20: "))
                if g > 0 and g < 21:
                    if i < 7:
                        if g > m:
                            print(f"{g} is greater than the number.")
                            print("❤️  "*(7-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m > g:
                            print(f"{g} is smaller than the number.")
                            print("❤️  "*(7-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m == g:
                            print("You won!🎉🎉🎉🎉🥂🥂🍾🍾")
                            again()
                            break

                        
                    else:
                        print(f"{m} was the number.")
                        print("you Loss, Chances Overed!")
                        print("❤️  "*(7-i), "🤍  "*i, "<--- LifeMeter")
                        again()
                        break
                else:
                    print("Invalid Interger!!!")
            except ValueError:
                print("It's not an integer.")
    elif x == 5:
        
        while True:
            try:
                g = int(input("Guess a number between 1 to 20: "))
                if g > 0 and g < 21:
                    if i < 5:
                        if g > m:
                            print(f"{g} is greater than the number.")
                            print("❤️  "*(5-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m > g:
                            print(f"{g} is smaller than the number.")
                            print("❤️  "*(5-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m == g:
                            print("You won!🎉🎉🎉🎉🥂🥂🍾🍾")
                            again()
                            break

                        
                    else:
                        print(f"{m} was the number.")
                        print("you Loss, Chances Overed!")
                        print("❤️  "*(5-i), "🤍  "*i, "<--- LifeMeter")
                        again()
                        break
                else:
                    print("Invalid Interger!!!")
            except ValueError:
                print("It's not an integer.")
    else:
        
        while True:
            try:
                g = int(input("Guess a number between 1 to 20: "))
                if g > 0 and g < 21:
                    if i < 3:
                        if g > m:
                            print(f"{g} is greater than the number.")
                            print("❤️  "*(3-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m > g:
                            print(f"{g} is smaller than the number.")
                            print("❤️  "*(3-i), "🤍  "*i, "<--- LifeMeter")
                            i += 1
                        elif m == g:
                            print("You won!🎉🎉🎉🎉🥂🥂🍾🍾")
                            again()
                            break

                        
                    else:
                        print(f"{m} was the number.")
                        print("you Loss, Chances Overed!")
                        print("❤️  "*(3-i), "🤍  "*i, "<--- LifeMeter")
                        again()
                        
                        break
                else:
                    print("Invalid Interger!!!")
            except ValueError:
                print("It's not an integer.")

#------------------------------------------------------------------------------------------------------------------------
# This block will call choose() function.

def main():
    choose()

#-------------------------------------------------------------------------------------------------------------------------
# Where it all started.
# Calling main function.

main()