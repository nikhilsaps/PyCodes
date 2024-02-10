# this  function takes  the file and conver it in to sting of lines

def ltoSO():
    f=open("nikhil.txt","r+")
    text=f.read()
    f.close()
    words = text.split(" ")

    return words

def main():
    print("start")
    lword=""
    for x in ltoSO():
        if len(x)>len(lword):
            lword=x
    print(lword)



if __name__ == "__main__":
    main()
