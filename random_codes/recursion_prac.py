def recur(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else :
        return recur(a-1)+recur(a-2)


for x in range(10):
    print(recur(x))
