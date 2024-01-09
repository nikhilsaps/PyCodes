class emp:
    def __init__(self,name, age,ids):
        self.name=  name
        self.age=age
        self.id =ids
    def show(self):
        print( f"Name : {self.name} \n Age:{self.age} \n Id :{self.age}")



class prog(emp):
    def showl(self):
        print("the default language is  show language")



def  main():
    p= prog("nikhil", 18,100)
    p.show()
    p.showl()


if __name__ =="__main__":
    main()