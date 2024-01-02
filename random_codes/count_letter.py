# count the occurence of the letter in string

txt="my name is nikhil"
lst_letter= []
count=0
for x in txt :
    if x not in lst_letter:
        lst_letter.append(x)
lst_letter.sort()
print(lst_letter)

for y in lst_letter:
    l=len(txt)-1
    count =0
    while(l>0):
        if y ==txt[l]:
            count+=1
        l-=1
    print(str(y)+ " :" +str(count))