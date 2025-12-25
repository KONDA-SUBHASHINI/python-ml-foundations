print("---Simple Calculator---")
a=float(input("Enter number 1:"))
b=float(input("Enter number 2: "))

print("1.Add \n 2.Subtrct \n 3.Multipliction \n 4.Division\n")
choice=int(input("Enter choice : "))
if choice==1:
    print(f"Addition of {a} and {b} is {a+b}")
elif choice==2:
    print(f"Subtrction of {a} and {b} is {a-b}")
elif choice==3:
    print(f"Multiplication of {a} and {b} is {a*b}")
elif choice==4:
    if(b!=0):
        print(f"Division of {a} and {b} is {a+b}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid Choice.")



