# Public access modifier :
class PublicExample:
    def __init__(self):
        self.name = "John" # Public attribute
    def display(self): # Public method
        print(f"Name: {self.name}")
obj = PublicExample()
print(obj.name) # Accessible
obj.display() # Accessible

#  Protected Access Modifier
class ProtectedExample:
    def __init__(self):
        self._age = 25 # Protected attribute
    def _display(self): # Protected method
        print(f"Age: {self._age}")
class Derived(ProtectedExample):
    def show(self):
        print(f"Accessing protected attribute: {self._age}")
        self._display()
obj = Derived()
obj.show()
print(obj._age) # Accessible, but not recommended

# Private Access Modifier
class PrivateExample:
    def __init__(self):
        self.__salary = 5000 # Private attribute
    def __display(self): # Private method
        print(f"Salary: {self.__salary}")
    def show(self): # Public method to access private data
        self.__display()
obj = PrivateExample()
obj.show() # Accessing private data via public method