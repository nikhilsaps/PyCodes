#binary search logic

array=[1,2,4,5,6,8,9,21,54,76,87,99]

num=int(input("enter the number you want to search"))

start=0
end = len(array)-1
mid = int((start+end)/2)
while(True):
    print("loop")
    mid = int((start + end) / 2)
    if array[mid]==num:
        print(f"got the number ${mid}")
        break
    elif array[mid]>num:
        end=mid

    else :
        start=mid+1


