

import random





def random_pass(n):
    randompass =""


    for x in range(n):
        randompass =randompass + str(random.randint(0,9))




    f=  open("otp.txt",'a')
    f.write(randompass+"\n")
    f.close()

    return  randompass





def main():
    print(random_pass(8))


if __name__ =="__main__":
    main()