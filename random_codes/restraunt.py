#the class  will contain the function to add something in menu

class restraunt:
    def __init__(self):
        self.menu={

        }

    def addM(self,item,price):
        self.menu[item]=price

    def rem (self,item):
        self.menu.pop(item)
    def showm(self):
        print(self.menu)



def main():
    p=restraunt()

    p.addM("salsa",100)
    p.addM("pizza",200)
    p.addM("burger",50)
    p.addM("marinara",150)
    p.showm()

    p.rem("burger")
    p.showm()


if __name__=="__main__":
    main()