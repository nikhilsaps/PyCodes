# implementation for stack

class Stack:
    def __init__(self,lst):
        self.lst=lst
    def __str__(self):
        return "sting out "
    def add(self):
        a=int(input("enter the number"))
        self.lst.append(a)

    def show(self):
        l=len(self.lst)-1
        while l>=0:
            print(self.lst[l])
            l-=1

    def clear(self):
        self.lst=[]

    def pop(self):
        self.lst.pop()
def main():
    lst =[1,2,3]
    stk=Stack(lst)
    while True:
        print(" main menu")
        print(" add ")
        print(" remove")
        print(" show")
        print(" clear")
        a= int(input("enter an option"))
        if a==1:
            stk.add()

        elif a==2:
            stk.pop()
        elif a==3:
            stk.show()
        elif a==4:
            stk.clear()
if __name__=="__main__":
    main()