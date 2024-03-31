#binary and decimal conversion

print(" Choose Conversion")
print("========================")
print("")
print(" 1 : Decimal to Binary")
print(" 2 : Binary to Decimal")
print(" 3 : Exit")
print("")
print("========================")


exit = True

choices = ["1", "2", "3"]

def conversion():
	
	choice = input("Enter choice: ")
	
	if choice not in choices:
		print("Enter option given")
		
	if choice == "1":
		d = int(input("Enter Decimal number: "))
		result = bin(d)[2:]
		print(f"{d} is equivalent to {result} in binary")
		
	if choice == "2":
		b = int(input("Enter Binary number: "))
		result = int(str(b), 2)
		print(f"{b} is equivalent to {result} in decimal")
		
	if choice == "3":
		exit = False
		quit()
		
		
while True:		
		conversion()
		