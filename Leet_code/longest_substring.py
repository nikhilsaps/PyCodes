


def main():
    data =[x for x in input("enter the string")]
    i=0
    j=0
    k=0
    while j< len(data):
        if data[k] in data[i:j]:
            print(f"repeated char  {data[k]} at {k}")
            i=j
        else:
            print(data[i:j+1])
            k+=1
        j+=1


if __name__ == '__main__':
    main()