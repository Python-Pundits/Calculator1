def dec_to_base():
   
    print("A: base-2 ")
    print("B: base-8 ")
    print("C: base-16 ")
    
    base = input("Enter base ").lower()
    decimal = int(input("Enter decimal "))
    
# Convert decimal to binary        
    if base == "a":
        binary_num =  bin(decimal)[2:]
        print("Binary: ",binary_num)
        
    
# Convert decimal to octal
    if base == "b":
        octal_number = oct(decimal)[2:]
        print("Octal: ",octal_number)
        
        
    
# Convert decimal to hexadecimal
    if base == "c":
        hexadec =  hex(decimal)[2:]
        print("Hexadecimal: ",hexadec)
        

print("Conversion Of Bases")

print("1: Convert from decimal to other base ")
print("2: Convert from other base  to decimal ")
print("3: convert from base-n to other base ")
choice = int(input("choose conversion" ))

if choice == 1: 
    dec_to_base()
if choice != 1:
    print("not created yet")