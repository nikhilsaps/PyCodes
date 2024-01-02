#this is  my code
a=  "love is in the wind"

for x in a:
    count=0
    for y in a:
        if x==y:
            count+=1
        else:
            continue

    print(x,count)

