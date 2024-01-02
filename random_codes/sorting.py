#sorting algorithm

arr=[1,5,2,-1,4,3]

a=0
l=len(arr)-1

while(a<l):
    if arr[a] > arr[a + 1]:
        temp =arr[a]
        arr[a]=arr[a + 1]
        arr[a + 1]=temp
        continue
    a+=1

print(arr)