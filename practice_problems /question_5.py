# Level 1
# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in
# upper case. Also please include simple test function to test the class methods.

class MyClass:
    def __init__(self):
        pass
    def get_string(self):
        self.string=input("enter the string")
    def show_string(self):
        print(f"{self.string}")

p=MyClass()
p.get_string()
p.show_string()


# # Solution:
# class InputOutString:
#     def init(self):
#         self.s = ""
#     def getString(self):
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()