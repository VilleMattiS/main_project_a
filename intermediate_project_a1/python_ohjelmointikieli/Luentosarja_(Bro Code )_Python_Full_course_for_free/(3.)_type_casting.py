#Type casting: changing the datatype of Variable A from datatype b to datatype c.
"""
NEW
Typecasting functions
int(a) == a to integer
float(a) == a to floating point
str(a) == a to string(array of characters)
bool(a) == a to boolean value
type(a) == datatype of a
"""


auto = "Mercedes"
model_year = 1998
is_fit_for_public_road = True
amount_of_fuel_in_litres  = 5.7



#type function gives the datatype of a variable and takes as input the variable
print(type(model_year))



#Typecasting to integer
"""
TypeCasting FROM float TO integer GIVES floor of the float AS integer
Typecasting FROM bool TO integer GIVES 1 XOR 0 as integer

"""
amount_of_fuel_in_litres = int(amount_of_fuel_in_litres)
print(amount_of_fuel_in_litres)
is_up_bool = True
is_up_integer = int(is_up_bool)
print(is_up_integer)



#Typecasting to bool
"""
typecasting 1 FROM integer TO bool gives True
typecasting 0 FROM integer TO bool gives False

typecasting non-empty string FROM string TO bool gives True
typecasting empty string FROM string TO bool gives False

"""
numberOne_integer = 1
numberSecondOne_integer = 0
number_boolean = bool(numberOne_integer)
numberSecondOne_boolean = bool(numberSecondOne_integer)
print(number_boolean)
print(numberSecondOne_boolean)



#Typecasting to string
"""
typecasting 1 FROM bool TO string GIVES True as string
typecasting 0 FROM bool TO string GIVES False as string
typecasting FROM float XOR int TO string GIVES the number as string

"""
truth_statement_one_bool = True
truth_statement_one_string = str(truth_statement_one_bool)
numberTwo_floating_point = 1235.4325
numberTwo_string = str(numberTwo_floating_point)
print(numberTwo_string)
print(f"bool -> string:{truth_statement_one_bool} -> {truth_statement_one_string}")


#Typecasting to floating point number
number_three_integer = 5000
number_three_floating_point = float(number_three_integer)
print(number_three_floating_point)




