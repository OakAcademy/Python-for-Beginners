def is_Prime(Number):
    if (Number == 1):
        return False
    elif (Number == 2):
        return True
    else:
        for i in range(2, Number):
            if (Number % i == 0):
                return False
            return True


while True:
    Number = input("Please enter a positive number: ")
    if Number == "q":
        break
    else:
        Number = int(Number)

        if (is_Prime(Number)):
            print(Number, " is a prime number")
        else:
            print(Number, " is not a prime number")