# Level 1
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
# (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.



#solution

def  main():
    val=[]
    for i in range(2000, 3200):
        if i%7==0 and i%5!=0:
            val.append(str(i))
    print(",".join(val))


if __name__=="__main__":
    main()


# there Solution
#
#     l = []
#     for i in range(2000, 3201): if
#     (i % 7 == 0) and (i % 5 != 0): l.append(str(i))
#     print(‘, ’.join(l)) 