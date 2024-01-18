# ### Question 64
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.


def sum(n):
    sum=0.0
    for x in range(1,n+1):
        sum += float(x)/(x+1)
    return sum


def main():
    ans= sum(5)
    print(ans)

if __name__ == '__main__':
    main()
# def sum_series(n):
#     total_sum = 0.0
#     for x in range(1, n+1):
#         total_sum += float(x) / (x + 1)
#     return total_sum
#
# def main():
#     ans = sum_series(5)
#     print(ans)
#
# if __name__ == '__main__':
#     main()