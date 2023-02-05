# 1
class AtLeastTwoMethods:
    some = str()
    def getString(self):
        self.some = input("Enter a string => ")
    def printString(self):
        print(self.some.upper())


a = AtLeastTwoMethods()
a.getString()
a.printString()

# 2
class Shape:
    lenght = 0
    def area(self):
        print(self.lenght)

class Square(Shape):
    def __init__(self, lngh):
        self.lenght = lngh
    def area(self):
        print(self.lenght * self.lenght)
    
    
b = Shape()
c = Square(5)

b.area()
c.area()
        
# 3 

class Rectangle(Shape):
    def __init__(self,length, width):
        self.lenght = length
        self.width  = width
    def area(self):
        print(self.lenght * self.width)

d = Rectangle(2,3)
d.area()

# 4

class Point():
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
    def show(self):
        print(f"Point 1 is on {self.point1}, and Point 2 is on {self.point2}")
    def move(self):
        print("Enter new values of points")
        self.point1 = int(input("Point 1 = "))
        self.point2 = int(input("Point 2 = "))
    def dist(self):
        print(f"The distances between points is {abs(self.point1 - self.point2)}")
        
f = Point(1,1)
f.show()
f.dist()
f.move()
f.dist()

# 5
class Account:
    limit = 10_000_000
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep):
        if self.balance + dep > self.limit:
            print("Your account cant be overdrawn")
        else:
            self.balance += dep
    def withdraw(self,output):
        if self.balance >= output:
            self.balance -= output
        else:
            print("You dont have enough money")

g = Account("Aidar",5000)
g.withdraw(5001)
g.deposit(1000000000000)

# 6

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

numbers = [2,34,5,6,234,5,6]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
