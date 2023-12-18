#pangram is  a worrd or  string that contains every leter of other string and  no repitition

s= "love"
b="ovlee"

sl=list(s)
print(sl)
sl.sort()
bl=list(b)
bl.sort()

print(sl,bl )
if sl==bl:

    print("panagram")
else:
    print("normal string")


