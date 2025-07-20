def pattern(p):
   
            # for i in range(p):
            #     print("*  " * i)
            # break
            i = 1
            while i <= p:
                print("*  " * i)
                i += 1
            

while True:
    p = int(input("What's p? "))
    if p > 0:
       pattern(p)
       
       break

        