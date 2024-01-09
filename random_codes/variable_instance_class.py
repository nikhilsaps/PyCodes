
class Emp:
    def  __init__(self, name):
        self.name =name
    def show(self):
        print(self.name)




def  main():
    e= Emp("nikhil")
    e.show()
    



if __name__=='__main__':
    main()
