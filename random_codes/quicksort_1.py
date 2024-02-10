# the code will sort the array to  quicksort logic
lst = [1,3,6,2,9,5,-1]
def partition(l,h):
    piv= lst[l]
    i=l
    j=h
    while(i<j):
        while lst[i] <= piv:
            i += 1
        while lst[j] > piv:
            j -= 1
        if (i < j):
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    return j


def qs(l,h):
    if(l<h):
        j=partition(l,h)
        qs(l,j)
        qs(j+1,h)






l=0
h=len(lst)-1

qs(l,h)

print(lst)