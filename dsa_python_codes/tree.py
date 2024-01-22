class Node:
    def __init__(self,data):
        self.left=None
        self.data =data
        self.right=None



class tree:
    def __init__(self):
        self.head=None

    def insert(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            print("Insertion at the top")
        else:
            print("Node exists, so moving")
            currentnode = self.head
            print(currentnode.data)

            while True:
                if data > currentnode.data:
                    print("Move right")
                    if currentnode.right is None:
                        currentnode.right = Node(data)
                        print("Inserted to the right")
                        break
                    else:
                        currentnode = currentnode.right
                else:
                    print("Move left")
                    if currentnode.left is None:
                        currentnode.left = Node(data)
                        print("Inserted to the left")
                        break
                    else:
                        currentnode = currentnode.left

    def show(self):
        self.in_order_traversel(self.head)

    def in_order_traversel(self,node):
        if node is not None:
            self.in_order_traversel(node.left)
            print(node.data)
            self.in_order_traversel(node.right)






p=tree()
p.insert(1)
p.insert(2)
p.insert(-1)
p.insert(4)
p.insert(3)
p.insert(-2)

p.show()