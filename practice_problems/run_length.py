def encode(data_str):
    data_list= [x for x in data_str]
    new_str=[]
    i=0
    count = 1
    while i <len(data_list):

        j=i+1
        if j<len(data_list):
            if data_list[i]==data_list[j]:
                count+=1

            else:
                new_str.append(f"{data_list[i]}{count}")
                count=1
        else:
            new_str.append(f"{data_list[i]}{count}")

        i+=1

    return "".join(new_str)

def  decode(encodedstr):
    data_list= [x for x in encodedstr]
    new_list=[]

    for x in range(1,len(data_list),2):
        i=0
        while i < int(data_list[x]):
            new_list.append(f"{data_list[x-1]}")
            i+=1
    return "".join(new_list)




def  main():
    data_str= input("enter  the  string")
    encodedstring= encode(data_str)
    print(encodedstring)
    decodedstring= decode(encodedstring)
    print(decodedstring)

if __name__ == '__main__':
    main()

