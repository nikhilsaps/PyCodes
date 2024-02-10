lst= [1,2,3,4,5,6,7,8,9,11,2,3,44,3,31]
lst.sort()

a= int(input("enter the number to  fisn in the list "))

start =0
end = len(lst)-1
mid = (start + end) // 2
while start<=end:
    mid = (start + end) // 2
    if a==lst[mid]:
        print(f"got the number{mid}",)
        break

    elif a < lst[mid]:
        end=mid-1

    else :
        start=mid+1

