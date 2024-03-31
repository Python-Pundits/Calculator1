from standard import standard_calc
from scientific import scientific_calc
from binary import binary_calc

print("1: Standard ")
print("2: Scientific ")
print("3: Base conversion")

mode = int(input("Choose mode "))

if mode == 1:
    standard_calc()
    
if mode == 2:
    scientific_calc()
    
if mode == 3:
    binary_calc()