class Animal:
  def type(self):
    print("Various types of animals")

  def age(self):
    print("Age of the animal.")

class Rabbit(Animal):
  def age(self):
    print("Age of rabbit.")

class Horse(Animal):
  def age(self):
    print("Age of horse.")

animal = Animal()
rabbit = Rabbit()
horse = Horse()

for object in (animal,rabbit,horse):
  object.type()
  object.age()
