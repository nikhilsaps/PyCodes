# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class Test:
    def __init__(self,name,age):
        self.name =name
        self.age=age
    
    def getstr(self):
        print(f"ok the name is  {self.name} and age is {self.age}")
    def printstr():
        print(f"{lower(self.name)}")

def main():
    x= Test("nikhil",25)
    print(x.age)
    print(x.name)
    print(dir(x))

if __name__=="__main__":
    main()