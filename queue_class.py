#implementation of ques with py class

class queue:
    def __str__(self):
        pass
    def __init__(self,lst):
        self.lst=lst
    def add(self):
        num=int(input("enter the number"))
        self.lst.append(num)
    def remove(self):
        self.lst.pop(0)
    def show(self):
        for x in self.lst:
            print(x)
    def clear(self):
        self.lst=[]

def main():
    lst=[]
    que=queue(lst)
    print(" main menu")
    print(" add ")
    print(" remove")
    print(" show")
    print(" clear")
    while True:
        a = int(input("enter an option"))
        if a==1: que.add()
        if a==2: que.show()
        if a==3: que.remove()
        if a==4: que.clear()
        else :
            pass
if __name__ =="__main__":
    main()



