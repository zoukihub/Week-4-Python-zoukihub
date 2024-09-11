class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
        print("Hello my name is " + self.name +
         ", I am " + str(self.age) +
         " years old, and I am " + self.gender + ".")
  
p1 = Person("Kate", 21, "Female")
p1.introduce()

