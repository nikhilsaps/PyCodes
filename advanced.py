#  python program to read file and create
#f= open("nikhil.txt",'x')
f= open("nikhil.txt",'r+')

txt=f.read()
f.close()
print(txt)
new_file=open("nitya.txt",'a')
new_file.write(txt)
new_file.close

print