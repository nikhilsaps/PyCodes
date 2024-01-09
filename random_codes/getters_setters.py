class myclass:
    def __init__(self,value):
        self._value=value

    def show (self):
        print(self._value)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,n):
        self._value=n





def main():
    p=myclass(10)

    print(p.value)
    p.value = 20
    print(p.value)



if __name__ =="__main__":
    main()