import math

print("""

Please select the operation you want to do


1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exponent
6.Calculate BMI
7.Calculate the area of the triangle
8.Calculate the area of the square
9.Finding the square root

For exit press 0


""")

Operation = int(input("Select an Operation = "))

if Operation == 1:
    Number_1 = int(input("Please enter the first number: "))
    Number_2 = int(input("Please enter the first number: "))
    print("Result = ", Number_1+Number_2)

elif Operation == 2:
    Number_1 = int(input("Please enter the first number: "))
    Number_2 = int(input("Please enter the first number: "))
    print("Result = ", Number_1 - Number_2)
elif Operation == 3:
    Number_1 = int(input("Please enter the first number: "))
    Number_2 = int(input("Please enter the first number: "))
    print("Result = ", Number_1 * Number_2)
elif Operation == 4:
    Number_1 = int(input("Please enter the first number: "))
    Number_2 = int(input("Please enter the first number: "))
    print("Result = ", Number_1 / Number_2)
elif Operation == 5:
    Number_1 = int(input("Please enter the number: "))
    print("Result = ", Number_1 ** 2)
elif Operation == 6:
    Weight = int(input("Please enter your Weight: "))
    Height = int(input("Please enter your height in meters: "))
    print("Result = ", Weight / (Height **2))
elif Operation == 7:
    Base = int(input("Please enter the base: "))
    Height = int(input("Please enter the height: "))
    print("Result = ", (Base * Height)/2)
elif Operation == 8:
    Side = int(input("Please enter the length of side: "))
    print("Result = ", Side * Side)
elif Operation == 9:
    Number_1 = int(input("Please enter the number: "))
    print("Result = ", Number_1 ** 0.5 )
elif Operation == 0:
    print("Exiting Application..")
    exit()
else:
    print("Invalid Operation")