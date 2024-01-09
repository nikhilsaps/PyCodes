
def greet(fx):
    def mfx(*args,**kwargs):
        print("welcome")
        fx(*args, **kwargs)
        print("to our home")
    return mfx


@greet
def name():
    print("nikhil ")



name()

@greet
def add(a,b):
    print( a+b)



k=add(2,3)
print(k)