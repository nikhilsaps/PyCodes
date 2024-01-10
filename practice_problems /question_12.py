# Level 2
# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number
# is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

def all_even(number):
    num_list= list(number)
    # print(f"the num is {num_list}")
    for x in num_list:
        if int(x)%2==0:
            continue
        else :
            return False
    return number


def main():
    # num=input("enter the number").split(",")
    for x in range(1000,3000+1):
        if all_even(str(x)):
            print(x)
        # else:
        #     print("nothing")

if __name__=="__main__":
    main()

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0)and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         values.append(s)
# print(",".join(values))