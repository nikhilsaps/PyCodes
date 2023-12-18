#find common keys  in dictionary

d={
    1:"a",
    5:"k",
    3:"c",
    4:"d"
}
m={
    5:"k",
    3:"c",
    4:"d"
}
n={}

dl=list(d.keys())
ml=list(m.keys())
nl=[]
for x in dl :
    if x in ml:
        nl.append(x)

for x in nl:
    n[x]=d[x]


print(n)