#this function is an example of addition 
def calculator_addvalue(addvalue_x,addvalue_y):
    calc_add = addvalue_x + addvalue_y
    return calc_add
add_x = calculator_addvalue(100,30)
print(add_x)
#this function is an example of subtraction
def calculator_subtvalue(subtvalue_x,subtvalue_y):
    calc_subt = subtvalue_x - subtvalue_y
    return calc_subt
subt_x = calculator_subtvalue(148,24)
print(subt_x)
#this function is an example of multiplication
def calculator_multvalue(multvalue_x,multvalue_y):
    calc_mult = multvalue_x * multvalue_y
    return calc_mult
mult_x = calculator_multvalue(247,35)
print(mult_x)
#this function is an example of squaring two numbers 
def calculator_squarevalue(squarevalue_x,squarevalue_y):
    calc_square_1 = squarevalue_x * squarevalue_x
    calc_square_2 = squarevalue_y * squarevalue_y
    return calc_square_1, calc_square_2
square_x, square_y = calculator_squarevalue(8,9)
print("This prints the square of " +str(square_x))
print("This prints the square of " +str(square_y))
#this function does an example of division 
def division(div1,div2):
    calc_div = div1 / div2
    return calc_div
print(division(20,5))
print(division(30,10))
#this function gets a remainder 
def remainder (rem1,rem2):
    calc_rem = rem1 % rem2
    return calc_rem
print("The remainder is:" +  str(remainder(9,8)))
print("The remainder is:" +  str(remainder(18,43)))
#this function is testing to see if the math is done correctly 
def correctcheck(math1):
    if math1 == str(5+5):
     return " You are correct"
    if math1 == str(5):
     return " You are wrong"
math1 = str(10)
math1 = str(5)
print(correctcheck(math1))
