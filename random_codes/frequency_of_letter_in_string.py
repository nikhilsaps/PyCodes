#  this code will show you the frequency of the letter in the given string  using dictionary function

s= 'hi this is nikhil singh'

d={

}
letters = set(s)
print(letters)

for x in letters :
    count=0
    for y in s:
        if x==y:
            count+=1
    d[x]=count

print(d)

d.pop("n")
print(d)