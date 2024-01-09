
class  myclass():
    def __init__(self,val):
        self.value=val
    @staticmethod
    def add(a,b):
        return a+b




def  main():
    p= myclass(10)
    print(myclass.add(1,2))



if __name__=="__main__":
    main()
