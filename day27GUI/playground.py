def add(*args):
    print(args[0])
    
    sum=0
    for n in args:
        sum+=n
    return sum



print(add(1,5,6,2,4,5,6,8))

def calculate(n,**kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n *= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.colour=kw.get("colour")
        self.seats=kw.get("seats")

my_car=Car(make="Nissan")
print(my_car.model)

