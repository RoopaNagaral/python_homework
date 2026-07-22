import math

#Task 5

#Class Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
            
    def __str__(self):
        return f"{self.x}, {self.y}"
            
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

#class Vector  
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def __str__(self):
        return f"Vector: {self.x}, {self.y}"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

#Demonstration  
print("Point Tests")
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(5, 7)

print(p1)                           
print("p1 == p2:", p1 == p2)        
print("p1 == p3:", p1 == p3)        
print("Distance p1 - p3:", p1.distance_to(p3))

print("\nVector Tests")
v1 = Vector(1, 4)
v2 = Vector(3, 6)

print(v1)                           
print(v2)                           

v3 = v1 + v2
print("v1 + v2 =", v3)             

print("Distance v1 - v2:", v1.distance_to(v2)) 