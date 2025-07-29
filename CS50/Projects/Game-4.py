# Need work!!

from random import randint

m = randint(1,20)

print("Levels Available:")
print("Press 1 for EASY - (7 Lives)")
print("Press 2 for MODERATE - (5 Lives)")
print("Press 3 for HARD - (3 Lives)")


while True:
        try:
            c = int(input("Enter A Level: "))
                

            if c < 4 and c > 0:

                break
                
            else:
                print("Invalid Level")
                print("Levels Are 1, 2 & 3.")
    
        except ValueError:
            print("It's not an integer.")

if c == 1:
    print("You've choosed Level EASY.")
    print("You have total 7 lives.")
    print("❤️  "*7)
    i = 1

    while True:
        try:
            g = int(input("Guess A Number Between 1 To 20: "))
            if g > 0 and g < 21:
                if i != 7:
                    if g > m:
                        print(f"{g} is greater than the number.")
                        print("❤️  " * (7-i),"🤍 "*i)
                        i += 1 
                    elif g < m:
                        print(f"{g} is smaller than the number.")
                        print("❤️  " * (7-i),"🤍 "*i)
                        i += 1
            
                    elif g == m:
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 " *i)
                    print("You've Lost, Lifemeter is Empty.")
                    print(f"{m} is the number.")
                    break

                
         
                
            else:
                 print("Guess The Number Betwwen 1 to 100 only.")

        except ValueError:
             print("It's not an integer.")


elif c == 2:
    print("You've choosed Level MODERATE.")
    print("You have total 5 lives.")
    print("❤️  "*5)
    i = 1

    while True:
        try:
            g = int(input("Guess A Number Between 1 To 20: "))
            if g > 0 and g < 21:
                if i != 5:
                    if g > m:
                        print(f"{g} is greater than the number.")
                        print("❤️  " * (5-i),"🤍 "*i)
                        i += 1 
                    elif g < m:
                        print(f"{g} is smaller than the number.")
                        print("❤️  " * (5-i),"🤍 "*i)
                        i += 1
            
                    elif g == m:
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 " *i)
                    print("You've Lost, Lifemeter is Empty.")
                    print(f"{m} is the number.")
                    break

                
         
                
            else:
                 print("Guess The Number Betwwen 1 to 100 only.")

        except ValueError:
             print("It's not an integer.")




else:
    print("You've choosed Level HARD.")
    print("You have total 3 lives.")
    print("❤️  "*3)
    i = 1

    while True:
        try:
            g = int(input("Guess A Number Between 1 To 20: "))
            if g > 0 and g < 21:
                if i != 3:
                    if g > m:
                        print(f"{g} is greater than the number.")
                        print("❤️  " * (3-i),"🤍 "*i)
                        i += 1 
                    elif g < m:
                        print(f"{g} is smaller than the number.")
                        print("❤️  " * (3-i),"🤍 "*i)
                        i += 1
            
                    elif g == m:
                        print("You gussed it right.")
                        print("🍾🥂🎉🎉")
                        break
                else:
                    print("🤍 " *i)
                    print("You've Lost, Lifemeter is Empty.")
                    print(f"{m} is the number.")

                               
                
         
                
            else:
                 print("Guess The Number Betwwen 1 to 20 only.")

        except ValueError:
             print("It's not an integer.")

