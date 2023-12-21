#the code will implement the class

class car:
    def  __init__(self,name ,year):
        self.name =name
        self.year=year

    speed= 0
    def accela(self,acc):
        self.speed= self.speed + acc
        print(self.speed)

mycar=car("ford",1993)
yourcar=car("nissan",2023)


print(yourcar.year)
print(mycar.accela(4))
print(mycar.accela(9))
