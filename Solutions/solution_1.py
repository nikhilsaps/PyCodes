# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def main():
    a=[]
    print("hello starting")
    for x in range(1999,3201):
        if x%5 == 0 and x%7== 0 :
            print(f"{x} can be divided by 5 and 7")
            a.append(x)
        else:
            pass
    print(a)



if __name__ == "__main__":
    main()