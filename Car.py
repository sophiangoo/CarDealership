class Car:
    def __init__(self, used, miles, model):
        self.used = used
        self.miles = miles
        self.model = model

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_miles(self, miles):
        self.miles = miles

    def add_miles(self, new_miles):
        self.miles += new_miles

    def get_miles(self):
        return self.miles

    def is_used(self):
        return self.used

# Example usage:
car = Car(used=True, miles=10000, model="Model S")
print(car.get_model())   # Output: Model S
print(car.get_miles())   # Output: 10000
print(car.is_used())     # Output: True

car.set_model("Model X")
car.set_miles(20000)
car.add_miles(5000)

print(car.get_model())   # Output: Model X
print(car.get_miles())   # Output: 25000
print(car.is_used())     # Output: True
