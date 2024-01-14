# Question: Define a class, which have a class parameter and have a same instance parameter.


class MyClas:
    def __init__(self,name=10):
        self.name=name
    def show(self):
        print(f" data is  {self.name}")


p=MyClas(7)
p.show()