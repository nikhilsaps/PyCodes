# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be
# searched in the list.

num_list= [1,2,3,4,5,6,7,8,9,10,77,99,121]


def binsearch(n):
    a= 0
    b=len(num_list)-1
    while a<=b:
        mid= (a+b)//2
        if n==num_list[mid]:
            print(f"element found at {mid}")
            return mid
        elif n>num_list[mid]:
            a=mid+1
        else :
            b=mid-1

def main():
    print(binsearch(121))



if __name__=="__main__":
    main()
