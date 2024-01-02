import time
# program to fidn if strng is anagram or not
beg=time.time()
print("hello  nikhil")
txt = "abcdefghijklmno pq"
lst_of_alpha= []
l=len(txt)
for a in txt:
    if a not in lst_of_alpha:
        lst_of_alpha.append(a)
lst_of_alpha.sort()
print(lst_of_alpha)
txt2="abcd ef ghij klmon pp qq"
for x in txt2:
    if x not in lst_of_alpha:
        print("not anagram")
        break
end=time.time()
print(end -beg)