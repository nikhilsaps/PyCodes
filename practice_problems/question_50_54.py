class myclass :
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f" name is {self.name}")




def  main():
    me= myclass("nikhil")
    me.show()
    other = me

    other.name="assi"
    other.show()
    me.show()
if __name__ == '__main__':
    main()