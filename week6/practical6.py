# 1. Create class named Circle with attributes radius and color. 
import math

class Circle:
    def __init__(self,radius,color):
        self.radius=float(radius)
        self.color=color

        if type(self.radius) != float:
            raise TypeError(f'Must be Float or Int , instead {type(self.radius)} detected')
        if self.radius<0:
            raise ValueError (f'Radius must be a positive number , instead {(self.radius)} detected')
        if type(self.color) != str:
            raise TypeError(f'Must be of String type, instead {type(self.radius)} detected')

    def print(self):
        print(f' A {self.color} circle with radius {self.radius}')

    def __add__(self,other):
        return Circle(self.radius+other.radius,self.color)
    def __sub__(self,other):
        result = (self.radius-other.radius)
        if result <= 0:
            raise ValueError(f'Negative or Zero value for circle radius, the first radius must be greater than the second radius ')
        else:
            return Circle(round(result,2),self.color)
    def __mul__(self,other):
        return Circle(self.radius*other.radius,self.color)
    def __pow__(self,n):
        if not ((isinstance(n,int))or (isinstance(n,float))):
            raise TypeError (f'argument must be either int or float type, instead {type(n)} found')
        return Circle(round(self.radius ** float(n),2),self.color)

    def Area(self):
        return round(math.pi*(self.radius)**2,4)
    def Circumference(self):
        return round(2*math.pi *(self.radius),4)
    def __str__(self):
        return(f'{self.radius},{self.color}')

a=Circle(7.0,'red')
print(type(a.radius))
b=Circle(5.0,"green")
print(a-b,"a-b")
print(a**(-1),"a**b")
