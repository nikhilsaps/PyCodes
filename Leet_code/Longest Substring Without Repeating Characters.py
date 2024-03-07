s= "abcabcbb"


for x in range(len(s)):
    if s[x]==s[x+1]:
        print(s[x:])   
    print (x)