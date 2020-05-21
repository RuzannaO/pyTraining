
#1. Write a Python class for Roman Numeral (I, V, X ...). 
def roman2val(n):
    base_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(n)):
        if i > 0 and base_list[n[i]] > base_list[n[i - 1]]:
            int_val += base_list[n[i]] - 2 * base_list[n[i - 1]]
        else:
            int_val += base_list[n[i]]
    return int_val
class rom_num:
    def __init__(self,name):
        self.name=name
    def make_int(self):
        self.value=roman2val(self.name)
        return roman2val(self.name)
    def summup(self,n):
        self.value+=roman2val(n)
    def subtract(self,n):
        self.value-=roman2val(n)
    def multliply(self,n):
        self.value=self.value*roman2val(n)


print(roman2val('II'))
p1=rom_num('IV')
        
# 2. Create a class Person.

class Person:
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
        self.age="age NA"
        self.gender="gender NA"
        self.student="Student NA"
        self.__password="PWD NA"
    def  greet(self,second_person):
        return("welcome, dear", second_person)
    def Goodbye(self):
        return("Goodbye everyone!")
    def Favorite_num(self,num1):
        return("Hello,my favorite number is ",num1)
    def getAge(self,age_years):
            self.age=age_years
    def getGender(self,Gender):
            self.gender=Gender
    def getStudent(self,Student):
            self.student=Student
    def __getPassword(self,Password):
        self.__password=Password
        
        
        
# 3. Write classes named Polygon, Quadrilateral, Rectangle, Square which should be inhereted from higher classes.

import math
class Polygon:
    a = []
    def __init__(self,number_of_sides):
        self.n=number_of_sides

    def inputSides(self):
        for i in range (0,self.n):
            self.a.append(float(input()))

    def perimeter(self):
        if len(self.a)==2:
            return 2*(self.a[0]+self.a[1])
        else:
            if len(self.a)==1:
                return 4*self.a[0]
            else:
                return(sum(self.a))

class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)

class Rectangle(Quadrilateral):
    def __init__(self):
        super(Quadrilateral,self).__init__(2)

    def area(self):
        if len(self.a)==2:
            return Quadrilateral.a[0]*Quadrilateral.a[1]
        else:
            return Quadrilateral.a[0]**2

class Square(Rectangle):
    def __init__(self):
        super(Quadrilateral,self).__init__(1)




        
        
