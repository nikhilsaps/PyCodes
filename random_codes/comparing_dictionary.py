d={
    1:"a",
    2:"b",
    3:"c",
    4:"d"
}
m={
    1:"a",
    3:"c",
    2:"b",
    4:"d"
}
dl=list(d.keys())
ml=list(m.keys())
dl.sort()
ml.sort()

if dl==ml:
    for x in dl:
        if d[x] != m[x]:
            print("diff")
            break


