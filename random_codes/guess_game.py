import random

ran=int(random.random()*100)
while(True):
    a = int(input("enter the  number you bitch : "))
    print(ran)
    if a!=ran:
        if abs(a-ran) >10:
            print("hot")
        elif abs(a-ran) <6:
            print("hotter")
    else :
        print ("you got it bitch ")