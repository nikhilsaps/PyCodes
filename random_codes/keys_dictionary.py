#this program  check the list of the  dictionary

d={
    4:"d",
    1: "a",
    5:"e",

    2:"b",
    3:"c"
}

l=list(d.keys())
l.sort()
m={

}
for x in l:
    m[x]=d[x]

print(m)