# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. The
# transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then,
# the output should be: 500

data= [x for x in input("enter the  data string").split(" ") ]
money= {
    'Balance':0
}
for x in range(len(data)):
    if x%2==0:
        print(f"operation = {data[x]}")
        if(data[x]=='D'):
            money['Balance']=money['Balance']+int(data[x+1])
        elif(data[x]=='W'):
            money['Balance'] = money['Balance'] - int(data[x + 1])
    else :
        print(f"Num = {data[x]}")

print(f"the remaining balance will be {money['Balance']}")

# Solution:
# netAmount = 0
# while True:
# s = input()
# if not s:
# break
# values = s.split(" ")
# operation = values[0]
# amount = int(values[1])if operation=="D":
# netAmount+=amount
# elif operation=="W":
# netAmount-=amount
# else:
# pass
# print(netAmount)