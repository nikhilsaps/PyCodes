s=  "nikhil"
tup=set(s)
dic={

}
for x in tup:
    count=0
    for y in s:
        if x==y:
            count+=1
    dic[x]=count

print(dic)