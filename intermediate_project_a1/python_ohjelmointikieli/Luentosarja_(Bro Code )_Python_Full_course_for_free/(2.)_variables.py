#Variable is a container for a value that is of some datatype




"""
DEFAULT MAIN DATA TYPES IN PYTHON
1. string  -> Values: x is array of characters.
2. int     -> Values: -9223372036854775808 <= x <= 9223372036854775807 , x is integer.
3. float   -> Values: 2.2250738585072014e-308 <= x <= 1.7976931348623157e+308 , x is floating point number.
4. boolean -> Values: x = True XOR x = False = 1 XOR 0 , x is 1 XOR 0.

"""




#String Datatype
"""
String are defined by "" double quates, and the text goes into the double quotes.
"""
animal = "cat"
car_brand = "mercedes-benz"
car_model = "AMG"
car_alert = f"the {car_brand} is serviced"
print(animal[1])
print(f"The brand is {car_brand} and the model is {car_model}")

"""
In print(f"text {variable}") f is for formatting, and what string is next after f is formatted, 
and in the brackets {} can be placed a name of a variable, such that it will be formatted to the print functions string
"""



#int Datatype
"""
int datatype stores whole numbers, int is shortName for integer. (what are the smallest and biggest numbers that can be stored into int in python?)
"""

year = -9223372036854775807
sum = 2 + 3
print(year)
print(year + sum)



#float data type
"""
float datatype stores 'decimal' numbers. (what are the smallest and biggest numbers that can be stored into float in python?)
"""

pi_approximation = 3.14
print(pi_approximation)



#Boolean datatype
"""
Boolean data type stores true false values. True and False are also 1 and 0, and integer arithmetic can be done to boolean values 
"""

is_on = True
is_not_on = False

print(is_on)




#Assigment START -> Make four variables each different datatype

name = "Kalle"
age = 24
height = 1.81
is_student = True

print(f"{name} is {age} and he's height is {height} and also the fact that he is a student is {is_student}")
#Assigment END