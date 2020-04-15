Number = int(input("Please enter a number: "))

Value = 1
Sum = 0

while Value < Number:

    if Number % Value == 0:
        Sum += Value
    Value +=1

if Sum == Number:
    print(Number, "is a perfect number.")

else:
    print(Number, "is not a perfect number!")