#  program to implement  stack on the  list
def show():
    l=len(lst)-1
    while(l>=0):
        print(lst[l])
        l-=1
def pop():
    l=len(lst)-1
    lst.pop(l)
def insert(sen):
    lst.append(sen)

def empty():
    lst.clear()




lst=[]



print("*********************")
print("      main menu      ")
print("*********************")
print("       1 show         ")
print("       2  POP         ")
print("      3  Insert       ")
print("       4 Empty        ")
print("*********************")

while True:
    a=int(input("enter the number "))
    if a == 1:
        show()
    elif a == 2:
        pop()
    elif a == 3:
        sen = int(input("enter the  number to  insert"))
        insert(sen)
    elif a == 4:
        empty()


