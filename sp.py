from abc import ABC,abstractmethod
"""1. Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning it should have only one job or responsibility."""
# Before SRP
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Code to save user to database
        pass
    
    def send_welcome_email(self):
        # Code to send email
        pass


# After SRP: Split responsibilities into different classes
class DatabaseService:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        print(f"{self.name} is saved")

class EmailService:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def send_welcome_email(self):
        print(f"{self.name} is sent")
        

"""2. Open/Closed Principle (OCP)
A class should be open for extension but closed for modification. 
This means you should be able to add new functionality without changing existing code."""

# Before OCP
class Discount:
    def __init__(self,product,price):
        self.product=product
        self.price=price

    def calculate(self):
        if self.product == "electronics":
            return self.price * 0.1
        elif self.product == "clothing":
            return self.price * 0.2

        


# After OCP: Add new categories without modifying Discount class
class Discount:
    def __init__(self,product,price):
        self.product=product
        self.price=price

    def calculate(self):
        raise NotImplementedError

class ElectronicsDiscount(Discount):

    def calculate(self):
        return self.price * 0.1

class ClothingDiscount(Discount):

    def calculate(self):
        return self.price * 0.2


"""3. Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of a subclass without"
 affecting the correctness of the program."""
 # Before LSP
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches cannot fly")

# After LSP: Avoid breaking behavior for subclasses
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")


"""4. Interface Segregation Principle (ISP)
A client should not be forced to implement interfaces it doesn't use. 
In other words, create smaller, more specific interfaces rather than large, general ones."""
# Before ISP
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        pass
    
    def eat(self):
        raise Exception("Robots don't eat")

# After ISP: Split responsibilities into smaller interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("I can work")
    
    def eat(self):
        print("I can eat")

class Robot(Workable):
    def work(self):
        print("I can work")


"""5.DIP 
Abstractions should not depend upon details. Details should depend upon 
abstractions."""
# Before DIP
class LightBulb:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb
    
    def operate(self):
        self.bulb.turn_on()  # Switch depends directly on LightBulb


# After DIP: Use abstraction (interface)
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass


class LightBulbWhite(Switchable):
    def turn_on(self):
        print("turn on White")

    def turn_off(self):
        print("turn off")

class LightBulbRed(Switchable):
    def turn_on(self):
        print("turn on Red")

    def turn_off(self):
        print("turn off")


class Switch:
    def __init__(self, device: Switchable):
        self.device = device
    
    def operate(self):
        self.device.turn_on()
