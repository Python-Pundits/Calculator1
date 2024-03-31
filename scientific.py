def scientific_calc():
    print("coming soon ")

import math

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

def pi():
    result = 3.1415926535897932384626433832795028841971
    return result

def exp():
    result = 2.7182818284590452353602874713526624977572
    return result

def factorial(a):
    if a == 1:
        return 1
    else:
        return n * factorial(a-1)


function_dict1 = {
    'sin'  : sin,
    'cos'  : cos,
    'tan'  : tan,
    'asin' : asin,
    'acos' : acos,
    'atan' : atan,
    'sqrt' : square_root,
    'pi'   :pi,
    'log'  :log,
    'ln'   :ln,
    'e'    :exp,
    '!'    :factorial
}

function_dict2 = {
    '^': power
}

def calculate(equation):
    variable = equation.split()
    for i in range(0,len(variable)):
        if variable[i] in function_dict1:
            print(function_dict1[variable[i]](int(variable[i + 1])))

        elif variable[i] in function_dict2:
            print(function_dict2[variable[i]](int(variable[i - 1]), (int(variable [i + 1]))))

        else:
            print(eval(variable[i]))

equate = input('Input your equation')
print (calculate (equate))