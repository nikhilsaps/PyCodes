# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=""
        n2=""
        while l1!=None:
            n1= n1+str(l1.val)
            l1=l1.next
        while l2!=None:
            n2= n2+str(l2.val)
            l2=l2.next
        
        sum= str(int(n1[::-1])+int(n2[::-1]))
        
        mynode= ListNode()
        for x in sum[::-1]: 
            if mynode.val is 0:
                mynode.val =x
                mynode.next=None
            else:
                temp =mynode
                while temp.next!=None:
                    temp =temp.next
                temp.next=ListNode(x)
        return mynode


            

       