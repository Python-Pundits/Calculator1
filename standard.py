def standard_calc():
    print("Choose Operation")   
    print("A : Addition")
    print("B : Subtraction")
    print("C : Multiplication")
    print("D : Division")
    print("E : Exit")
    
    
    exit = True
    while exit == True:
        
        choice = str(input("Enter choice")).lower()
        
        if choice == "a":
            a = float(input("Enter first number"))
            b=float(input("Enter Second number"))
            result = a + b
            print(round(result,3))
                
        if choice == "b":
            a = float(input("Enter first number"))
            b= float(input("Enter Second number"))
            result = a - b
            print(round(result,3))
                
        if choice == "c":
            a = float(input("Enter first number"))
            b= float(input("Enter Second number"))
            result = a * b
            print(round(result, 3))
                
        if choice == "d":
            a = float(input("Enter first number"))
            b= int(input("Enter Second number"))
            result = a / b
            print(round(result, 3))
            
        if choice == "e":
            exit = False  