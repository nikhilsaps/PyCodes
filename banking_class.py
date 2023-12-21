# thei code in python will implement and  work with banking and  dep/ with

class Pacnt:
    bank_name ="indus valley bank"
    def __init__(self,name ,balance ):
        self.name=name
        self.balance=balance
    def deposit(self,amnt):
        self.balance=self.balance+amnt

    def withdraw(self,amnt):
        self.balance=self.balance-amnt

    def show_amnt (self):
        print(self.name,self.balance)


def main():
    p1= Pacnt("nikhil",100)

    print(p1.show_amnt())
    print(p1.deposit(100))
    print(p1.show_amnt())
    print(p1.withdraw(20))
    print(p1.show_amnt())




if __name__=="__main__":
    main()