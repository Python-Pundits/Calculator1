def dec_to_base():

    print("A: Binary ")
    print("B: Octal ")
    print("C: Hexa ")

    base = input("Enter Base: ").lower()
    decimal = int(input("Enter Decimal "))

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
        
def bin_to_base():
    print("A: Decimal ")
    print("B: Octal ")
    print("C: Hexa ")

    base = input("Enter Base: ").lower()
    binary = input("Enter Binary number: ")

    # Convert binary to decimal
    if base == "a":
    	decimal = int(str(binary), 2)
    	print("Decimal: ", decimal)
    

    # Convert binary to octal
    if base == "b":
        octal_number = oct(decimal)[2:]
        print("Octal: ", octal_number)

    # Convert binary to hexadecimal
    if base == "c":
        hexadec = hex(decimal)[2:]
        print("Hexadecimal: ", hexadec)
        
def oct_to_base():

    print("A: Binary ")
    print("B: Decimal ")
    print("C: Hexa ")

    base = input("Enter Base: ").lower()
    octal = input("Enter Octal number: ")

    # Convert octal to binary
    if base == "a":
        binary_num = bin(decimal)[2:]
        print("Binary: ", binary_num)

    # Convert octal to decimal
    if base == "b":
        decimal = int(octal, 8)
        print("Decimal: ", decimal)

    # Convert octal to hexadecimal
    if base == "c":
        hexadec = hex(decimal)[2:]
        print("Hexadecimal: ", hexadec)


print("Conversion of Bases")
print("========================")
print("")
print("1: Decimal to Other Bases ")
print("2: Binary to Other Bases")
print("3: Octal to Other Bases ")
print("4: Hexa to Other Bases")
print("5: Exit")
print("")
print("========================")
choice = int(input("Choose Operation: " ))



	
if choice == 1: 
    dec_to_base()
if choice == 2:
    bin_to_base()
if choice == 3:
	oct_to_base()