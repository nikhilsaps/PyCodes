class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            currentnode = self.head
            while (currentnode.next):
                currentnode = currentnode.next
            currentnode.next = newnode
    def insert_beg(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insert_sep(self, data, index):
        newnode = Node(data)
        position = 0
        currentnode = self.head
        if position == index:
            self.insert_beg(data)
        else:
            while (currentnode != None and position != index):
                position += 1
                currentnode = currentnode.next
            if currentnode != None:
                newnode.next = currentnode.next
                currentnode.next = newnode
            else:
                print("wrong index")

    def remove_que(self):
        if self.head is None:
            print("removing from a  already  empty LL")
        else:
            self.head=self.head.next

    def remove_stack(self):
        if self.head is None:
            print("messing up with an empty LL")
        elif self.head.next is None:
            # If there is only one element in the list
            self.head = None
        else:
            currentnode = self.head
            while currentnode.next.next:
                currentnode = currentnode.next
            currentnode.next = None

    def remove_sep(self, index):
        pos = 0
        currentnode = self.head
        if self.head is None:
            print("empty LL")
        else:
            if pos == index:
                self.remove_que()
            else:
                while (currentnode != None and pos + 1 != index):
                    pos += 1
                    currentnode = currentnode.next
                if currentnode!=None:
                    currentnode.next = currentnode.next.next

                else:
                    print("wrong index")

    def show(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

    def update(self, value, index):
        pos = 0
        currentnode = self.head
        if self.head is None:
            currentnode.data = value
        else:
            while (currentnode != None and pos != index):
                pos += 1
                currentnode = currentnode.next
            if currentnode != None:
                currentnode.data = value



def main():
    Llist=Linkedlist()
    while True:
        print("1.insert_sep \n 2. insert_beg \n 3. insert_end\n")
        print("4.remove_sep \n 5. remove_beg \n 6. remove_end\n")
        print("9.update \n 10. show \n 11. clear")



        a=int(input("enter the options for above "))
        match a:
            case 1:
                index=int(input("enter the index"))
                data=int(input("enter the value"))
                Llist.insert_sep(data,index)
            case 2:
                data = int(input("enter the value"))
                Llist.insert_beg(data)
            case 3:
                data = int(input("enter the value"))
                Llist.insert_end(data)
            case 4:
                index = int(input("enter the index"))
                Llist.remove_sep(index)
            case 5:
                Llist.remove_que()
            case 6:
                Llist.remove_stack()
            case 7:
                Llist.show()
            case 8:
                index = int(input("enter the index"))
                data = int(input("enter the value"))
                Llist.update(index=index,value=data)
            case 9:
                pass
            case 10:
                pass
            case _:
                pass



if __name__=='__main__':
    main()