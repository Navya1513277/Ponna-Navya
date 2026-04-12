# # Single inheritance :
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return "Animals makes a sound"
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!" 
# obj=Dog("dog")
# print(obj.speak())          

# # Multiple inheritance :
# class Bird:
#     def fly(self):
#         print("I can fly")
# class Fish:
#     def swim(self):
#         print("I can swim")
# class Duck(Bird,Fish):
#     def quack(self):
#         print("Quack! quack") 
# duck=Duck()           
# print(duck.fly())             
# print(duck.quack())


# #  Multilevel Inheritance
# class Vechicle:
#     def info(self):
#         return "This is a vechicle"
# class Car(Vechicle):
#     def car_info(self):
#         return "This is car"
# class ElectricCar(Car):
#     def battery_info(self):
#         return "This car runs on eletricity" 
# ele=ElectricCar()
# print(ele.info())
# print(ele.car_info())
# print(ele.battery_info())       

# # Hierarchical Inheritance :
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return "Same generic animal sound" 
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!"
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Memo!"
# class Cow(Animal):
#     def speak(self):
#         return f"{self.name} says moo!" 
# dog=Dog("Buddy")
# cat=Cat("whiskers")
# cow=Cow("Daisy")
# print(dog.speak())
# print(cat.speak())
# print(cow.speak())
       


   
