class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head= None
    def insert_end(self,data):
        if self.head is None:
            newnode =Node(data)
            self.head=newnode
        else:
            newnode=Node(data)
            currentnode=self.head
            while(currentnode.next):
               currentnode=currentnode.next
            currentnode.next=newnode

    def insert_beg(self, data):
        newnode=Node(data)
        if self.head is None:
            self.head =newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insert_sep(self,data,index):
        newnode=Node(data)
        position =0
        currentnode=self.head
        if position ==index :
            self.insert_bg(data)
        else :
            while (currentnode!=None and position !=index):
                position+=1
                currentnode = currentnode.next
            if currentnode!=None:
                newnode.next=currentnode.next
                currentnode.next=newnode
            else:
                print("wrong index")


    def show(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next
    def remove_que(self):
        if self.head is None:
            print("removing from a  already  empty LL")
        else:
            currentnode=self.head
            currentnode=currentnode.next
            self.head=currentnode
    def remove_stack(self):
        if self.head is None:
            print("messingh up with  empty LL")
        else:
            currentnode= self.head
            while(currentnode.next.next):
                currentnode=currentnode.next
            currentnode.next=None

    def remove_sep(self,index):
        pos=0
        currentnode=self.head
        if self.head is None:
            print("empty LL")
        else :
            if pos == index:
                self.remove_que()
            else:
                while (currentnode!=None and pos+1!=index):
                    pos+=1
                    currentnode=currentnode.next

                currentnode.next=currentnode.next.next



    def update(self):
        pass



def main():

    Llist=Linkedlist()
    Llist.insert_end(1)
    Llist.insert_end(2)
    Llist.insert_end(3)
    Llist.insert_end(4)
    Llist.insert_end(5)
    Llist.show()
    Llist.remove_sep(2)
    Llist.show()




if __name__=='__main__':
    main()
