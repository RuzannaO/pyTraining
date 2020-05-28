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


# 2. For Roman Numeral class from previous homework override basic mathematical operations (+,-,*,//,**)
class RomanNumber:
    def __init__(self, roman_number):
        self.number = roman_number
        if not (isinstance(self.number, str)):
            raise TypeError(f'input must be a string, another type is detected!  {self.number}  {type(self.number)}')
        if (any(x.islower() for x in self.number)):
            raise IOError('Incorrect input, no lowercase letters allowed!   %s  ' % self.number)

    def get_num(self):
        return self.number

    def set_num(self, num1):
        self.number = num1
    def convert_to_roman(self, num):

        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        if not 0 < num < 4000:
            raise ValueError(f'Argument must be between 1 and 3999, we got {num}')
        assert (isinstance(num,int) and num > 0),(f'make sure the number is a positive integer, we got {num}')
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    def convert_to_num(self):
        num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        try:
            for key, value in enumerate(self.number):
                if (key + 1) == len(self.number) or num_dict[value] >= num_dict[self.number[key + 1]]:
                    result += num_dict[value]
                else:
                    result -= num_dict[value]
        except KeyError:
            raise ValueError ('input is not a valid Roman numeral: %s' % self.number)

        if self.convert_to_roman(result)!=self.number:
            raise IOError (f'Invalid input, can not read as a Roman numeral {self.number}')
        else:
            return result
    def __str__(self):
        return (f'{self.number}')
    def __add__(self, other):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() + other.convert_to_num()))
    def __sub__(self, other):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() - other.convert_to_num()))
    def __mul__(self, other):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() * other.convert_to_num()))
    def __pow__(self,pow):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() ** pow))
    def __floordiv__(self, other):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() // other.convert_to_num()))


a=RomanNumber("MMMCMXCIX")
b=RomanNumber(["L"])
print((a))


# 3 Class Person


class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        print(type(gender))
        assert (not(list(x for x in [name,last_name,gender,password] if type(x)!=str))),"name,last_name,gender,pasword - all must be string values. Please, check again!"
        assert ((isinstance(age,int)) and age<=150 and age>0), "Age input should be integer between 0 to 150"

        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password = password

        if isinstance(student, bool):
            self.student = student
        else:
            raise Exception("Student attribute takes values True or False")

    def Read_file(self,filename):
        assert (isinstance(filename,str)),"only string input accepted for filename"
        assert (len(list(x for x in filename if x in ('/\:*"<>|')))==0),"Invalid input character"
        assert (filename[0]!=" " and filename[-1]!=" "), "Please remove space character at the start and/or end of the filename."
        fullname=filename+'.txt'
        try:
            print(fullname)
            open(fullname)
        except FileNotFoundError as e:
            print("no such file exists")

    def Greeting(self, second_person):
        if not(isinstance(second_person,str)):
            raise TypeError (f'Please enter string value for person name')
        else:
            return f'Welcome dear {second_person}!'

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        if not(isinstance(num1,int)):
            raise TypeError (f'Please enter integer value for the favorite number.')
        else:
            return 'My favorite number is {}'.format(num1)

a=Person("arman","Petrosyan",100,"Male",True,"kokokok")

# 4. For Polygon, Quadrilateral, Rectangle and Square classes from the previous homework add validations of number of sides.
class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = list()

    def input_sides(self, sides):
        self.sides = sides
        if not(isinstance(self.sides,list)):
            raise TypeError ('input must be a list, another type is detected!   %s ' % type(self.sides))
        assert len([x for x in self.sides if isinstance(x,str)])==0, "no str value acceptable for a side"
        assert len(self.sides) == self.n, "Incorrect number of sides"
        assert len([x for x in self.sides if x<0])==0, "you have entered a negative value for a side"
        assert len([x for x in self.sides if isinstance(x,bool)])==0, "no boolean value acceptable for a side"

    def disp_sides(self):

        assert len(self.sides)!=0, "No sides data entered"
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])

    def get_perimeter(self):
        return sum(self.sides)

class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)

class Rectangle(Quadrilateral):
    #     def __init__(self):
    #         super().__init__()
    def input_sides(self, s):
        super().input_sides(s * 2)
        print(len(self.sides),self.n)
    def get_area(self):
        return self.sides[0] * self.sides[1]

class Square(Rectangle):
    #     def __init__(self):
    #         super().__init__()
    def input_sides(self, s):
        super().input_sides(s * 2)


a=Rectangle()
a.input_sides([2,2.2])
print(a.disp_sides())
print(a.get_perimeter())
# print(a.get_area())





