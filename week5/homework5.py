
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
        self.student=False
        self.__password="PWD NA"
    def  greet(self,second_person):
        return("welcome, dear", second_person)
    def Goodbye(self):
        return("Goodbye everyone!")
    def Favorite_num(self,num1):
        return("Hello,my favorite number is ",num1)
    def setAge(self,age_years):
            self.age=age_years
    def setGender(self,Gender):
            self.gender=Gender
    def setStudent(self,Student:bool):
            self.student=Student
    def __getPassword(self,Password):
        self.__password=Password

x=Person("Arman","Petrosyan")

print(x.student)
x.setStudent(True)
print(x.student)
        
        
        
# 3. Write classes named Polygon, Quadrilateral, Rectangle, Square which should be inhereted from higher classes.

class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = list()

    def input_sides(self, sides):
        self.sides = sides

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])

    def get_perimeter(self):
        return sum(self.sides)

class Quadrilateral(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)

class Rectangle(Quadrilateral):
    def __init__(self):
        super(Quadrilateral,self).__init__(2)

    def area(self):
        if len(self.sides)==2:
            return self.sides[0]*self.sides[1]
        else:
            return self.sides[0]**2
class Square(Rectangle):
    def __init__(self):
        super(Quadrilateral,self).__init__(1)



a1=Quadrilateral()
a1.input_sides([1,2,3,5])

print(a1.get_perimeter())




        
        
