class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"make: {self.make},model: {self.model}"

    
myCar = Car("Hyundai","Sonata")
print(myCar) #make: Hyundai, model: Sonata

