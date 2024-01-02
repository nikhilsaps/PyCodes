class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def insert_beg(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            currentnode = self.head
            while (currentnode.next):
                currentnode = currentnode.next
            currentnode.next = newnode
    def insert_end(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def insert_sep(self,data,index):
        newnode = Node(data)
        position = 0
        currentnode = self.head
        if position == index:
            self.insert_bg(data)
        else:
            while (currentnode != None and position != index):
                position += 1
            if currentnode != None:
                newnode.next = currentnode.next
                currentnode.next = newnode
            else:
                print("wrong index")
    def remove_beg(self):
        pass
    def remove_end(self):
        pass
    def remove_sep(self):
        pass
    def show(self):
        pass
    def update(self):
        pass



def main():
    Llist=Linkedlist()
    while True:
        print("1.insert_sep \n 2. insert_beg \n 3. insert_end\n")
        print("4.remove_sep \n 5. remove_beg \n 6. remove_end\n")
        print("9.update \n 10. show \n 11. clear")



        a=int(input("enter the options for above "))
        match a:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass



if __name__=='__main__':
    main()