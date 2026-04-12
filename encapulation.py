# Public Access Modifire:

# class PublicExample:
# def __init__(a):
# a.name = "John" # Public attribute
# def display(a): # Public method
# print(f"Name: {a.name}")
# obj = PublicExample()
# print(obj.name) # Accessible
# obj.display() # Accessible


# Protected access Modifire:

# class ProtectedExample:
# def __init__(self):
# self._age = 25 # Protected attribute
# def _display(self): # Protected method
# print(f"Age: {self._age}")
# class Derived(ProtectedExample):
# def show(self):
# print(f"Accessing protected attribute: {self._age}")
# self._display()
# obj = Derived()
# obj.show()
# print(obj._age) # Accessible, but not recommended