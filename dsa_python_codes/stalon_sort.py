def sorter(l):
    x=0
    while x<len(l):
        j=x+1
        if j<len(l):
            if l[x]>l[j]:
                l.pop(x)
                x=0
        x+=1

    return l


def main():
    print(sorter([9,1,4,3,2,5,7]))



if __name__ == '__main__':
    main()