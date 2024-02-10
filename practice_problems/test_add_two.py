def  add(a,b):
    c=a+b
    return c
    pass


def real_add(a,b):
    return a+b



def main():
    if add(1,2)==real_add(1,2):
        print("test  1  pass ")
    if add(3,4)==real_add(3,4):
        print("test  2  pass ")
    if add(4,7)==real_add(4,7):
        print("test  3  pass ")

if __name__ == '__main__':
    main()