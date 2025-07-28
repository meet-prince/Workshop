import random

while True:
    x = int(input("Enter a number between 1 to 10: "))

    if x > 0 and x < 11:
        

        m = random.randint(1,10)

        if x == m:
            print(f"{x} is the chosen one!")
            print("You Won!! :)")
            break

        else:
            print(f"{m} is the number computer selected.")
            print("You gussed it wrong! 😔")
            print("You Lost!")
            t = input("Do you wanna continue this game, Enter Y for yes or N for No (Y/N): ").title().strip()
            if t == "N":
                break
            
                    

