import math
import operator
from IPython.display import clear_output

def sin(a):
    result = math.sin(a)
    return result

def asin(a):
    result = math.asin(a)
    return result

def cos(a):
    result = math.cos(a)
    return result

def acos(a):
    result = math.asin(a)
    return result

def tan(a):
    result = math.acos(a)
    return result

def atan(a):
    result = math.atan(a)
    return result

def log(a):
    result = math.log(a)
    return result

def ln(a):
    result = math.log(a) * 2.303
    return result

def power(a,b):
    result = a ** b
    return result

def square_root(a):
    result = math.sqrt(a)

def pi(a):
    if a is None:
        result = 3.1415926535897932384626433832795028841971
    else:
        result = a * 3.1415926535897932384626433832795028841971
    return result

def exp(a):
    if a is None:
        result = 2.7182818284590452353602874713526624977572
    else:
        result = a * 2.7182818284590452353602874713526624977572
    return result

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

function_dict1 = {
    'sin'  : sin,
    'cos'  : cos,
    'tan'  : tan,
    'asin' : asin,
    'acos' : acos,
    'atan' : atan,
    'sqrt' : square_root,
    'π'    :pi,
    'log'  :log,
    'ln'   :ln
}

function_dict2 = {
    '^': power
}

function_dict3 = {
    'e'    :exp,
    '!'    :factorial
}

operation_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
def calculate(equation):
    variable = equation.split()
    ans = None
    operation = operator.mul
    for value in range(0, len(variable)):
        if  variable[value] in function_dict1:
            if ans is None:
                ans = function_dict1[variable[value]](int(variable[value + 1]))
            else:
                ans = operation(ans, function_dict1[variable[value]](int(variable[value + 1])))

        elif variable[value] in function_dict2:
            if ans is None:
                ans = function_dict2[variable[value]](int(variable[value - 1]), int(variable[value + 1]))
            else:
                if operation == operator.add:
                    result = int(ans - int(variable[value - 1]))
                    ans = operation(int(result), function_dict2[variable[value]](int(variable[value - 1]), int(variable[value + 1])))

                if operation == operator.sub:
                    result = int(ans + int(variable[value - 1]))
                    ans = operation(int(result), function_dict2[variable[value]](int(variable[value - 1]), int(variable[value + 1])))

                if operation == operator.mul:
                    result = int(ans) / int(variable[value - 1])
                    ans = operation(int(result), function_dict2[variable[value]](int(variable[value - 1]), int(variable[value + 1])))

                if operation == operator.truediv:
                    result = int(ans) * int(variable[value - 1])
                    ans = operation(int(result), function_dict2[variable[value]](int(variable[value - 1]), int(variable[value + 1])))
                print(result)

        elif variable[value] in function_dict3:
            if ans is None:
                ans = function_dict3[variable[value]](variable[value - 1])
            else:
                if operation == operator.add:
                    result = int(ans - variable[value - 1])
                    ans = operation(int(result), function_dict3[variable[value]](int(variable[value - 1])))

                if operation == operator.sub:
                    result = int(ans + variable[value - 1])
                    ans = operation(int(result), function_dict3[variable[value]](int(variable[value - 1])))

                if operation == operator.mul:
                    result = int(ans) / int(variable[value - 1])
                    ans = operation(int(result), function_dict3[variable[value]](int(variable[value - 1])))

                if operation == operator.truediv:
                    result = int(ans) * int(variable[value - 1])
                    ans = operation(int(result), function_dict3[variable[value]](int(variable[value - 1])))

        elif variable[value] in operation_dict:
            operation = operation_dict[variable[value]]

        elif variable[value].isdigit():
            if ans is None:
                ans = int(variable[value])

            elif variable[value - 1] in function_dict1:
               pass

            elif variable[value - 1] in function_dict2:
               pass

            else:
                ans = operation(ans, int(variable[value]))

        else:
            print('input not supported type h for help')

    print(ans)



def help():
    print (' ')
    print ('* Spaces must be in between integers, operators, function')
    print ('* space must be added after inputing value assign to the function' )
    print ('* more functions coming')
    print ('* operation on integers can be used but spaces must be in between integers and operators (e.g 5 + 5)')

print ('Functions')
print ('sin   cos   tan')
print ('asin  acos  atan')
print ('log   ln    e')
print ('^     !     π')
print (' ')
print (' ')
print ('h for help')
print ('x to exit')
print ('c to clear history')

exit = False

print(power(2,3))
while exit == False:
    equate = input('')
    if equate == 'x' or equate == 'X':
        print ('Good bye')
        exit = True

    elif equate == 'h' or equate == 'H':
        print (help())

    elif equate == 'c' or equate == 'C':
        clear_output()
        print ('Functions')
        print ('sin   cos   tan')
        print ('asin  acos  atan')
        print ('log   ln    e')
        print ('^     !     π')
        print (' ')
        print (' ')
        print ('h for help')
        print ('x to exit')
        print ('c to clear history')

    else:
        print (calculate (equate))