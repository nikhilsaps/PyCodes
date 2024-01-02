#geometric progression

a=int(input("enter the number"))
com_ratio=int(input("enter thr common ratio "))
term_count=int(input("enter count for terms you want "))
t=0
while(t<term_count):
    print (a*(com_ratio**t))
    t+=1


