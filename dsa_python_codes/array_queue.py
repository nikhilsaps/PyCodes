# the program will implement all the function of queue in  array


class queue:
    def __init__(self,lst=[]):
        self.lst=lst
    def __str__(self):
        return f"{self.lst}"

    def add(self,num):
        self.lst.append(num)

    def show(self):
        for x in self.lst:
            print(f"{x} \n")
    def remove(self,indi):
         self.lst.pop(indi)
    def update(self,indi,num):
        self.lst[indi]=num

    def clear(self, clear):
        self.lst.clear()



def main():
    p=queue()
    p.add



if __name__ =="__main__":
    main()