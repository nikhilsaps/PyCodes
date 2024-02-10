# Question: A website requires the users to input username and password to register. Write a program to check the validity of password
# input by users. Following are the criteria for checking the password: 1. At least 1 letter between [a-z] 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z] 3. At least 1 character from [$#@] 4. Minimum length of transaction password: 6 5. Maximum length of
# transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the
# above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are
# given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

def pwdcheck(pwd):
    flagal=0
    flagdig=0
    flaglow=0
    flagupp=0
    flagspc=0
    for char in pwd:
        if char.isalpha():
            flagal=1
        if char.isdigit():
            flagdig=1
        if char.islower():
            flaglow=1
        if char.isupper():
            flagupp=1
        if char in ['$', '@', '#']:
            flagspc=1
    if len(pwd)>6 and len(pwd)<12:
        if(flagal==1 and flagdig==1 and flaglow==1 and flagupp==1 and flagspc==1):
            print(f"good password {pwd}")
        else:
            print(f"failed password {pwd}")
    else:
        print(f"password length is incorrect ")



pwd_list =input("Enter the password").split(",")

print(pwd_list)
for pwd in pwd_list:
    pwdcheck(pwd)


# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
# if len(p)<6 or len(p)>12:
# continue
# else:
# pass
# if not re.search("[a-z]",p):
# continue
# elif not re.search("[0-9]",p):
# continue
# elif not re.search("[A-Z]",p):
# continue
# elif not re.search("[$#@]",p):
# continue
# elif re.search("\s",p):
# continue
# else:
# pass
# value.append(p)
# print(",".join(value))