# I didn't know much about Python Classes, but I did know about it in Java so it was easy to understand from w3schools.com
class Car():
  def __init__(self, make, model):
    self.make = make
    self.model = model
car1 = Car(2006, "Toyota")

print(car1.make)
print(car1.model)
