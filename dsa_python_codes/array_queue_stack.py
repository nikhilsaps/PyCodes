# the program will implement all the function of queue in  array
import os

class queue:
    def __init__(self,lst):
        self.lst=lst
    def __str__(self):
        return f"{self.lst}"

    def add(self):
        a=int(input("enter the number"))
        self.lst.append(a)

        self.show()

    def show(self):
        for x in self.lst:
            print(f"{x}")

    def remove(self):
        indi = int(input("enter the index"))
        self.lst.pop(indi)

        self.show()
    def update(self):
        indi = int(input("enter the index"))
        a = int(input("enter the number"))
        self.lst[indi]=a

        self.show()

    def clear(self):
        self.lst.clear()

        self.show()
    def removeque(self):
        self.lst.pop(0)

    def removestack(self):
        self.lst.pop(len(self.lst)-1)


def main():
    lst=[]
    p=queue(lst)
    while True:
        print("\n 1 show \n 2 add \n 3 update \n 4 remove \n 5 clear \n 6 querem \n 7 stackrem")
        a = int(input("enter the options"))
        match a:
            case 1:
                p.show()
            case 2:
               p.add()
            case 3:
                p.update()
            case 4:
                p.remove()
            case 5:
                p.clear()
            case 6:
                p.removeque()

            case 7:
                p.removestack()
            case _:
                pass
        # os.system('cls')





if __name__ =="__main__":
    main()