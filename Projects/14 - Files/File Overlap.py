O_List = [number for number in range(150) if number % 2 != 0]
P_List = []

for num in range(2,150):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       P_List.append (num)

with open("Numbers.txt", "w") as Odd_Numbers:
    for number in O_List:
        Odd_Numbers.write(str(number)+ ", ")

with open("Prime_Numbers", "w") as Prime_Numbers:
    for number in P_List:
        Prime_Numbers.write(str(number)+ ", ")

Overlap = []

for numbers in  P_List :
    if numbers in O_List:
        Overlap.append(numbers)

with open("Overlap_Numbers", "w") as Overlap_Numbers:
    for number in Overlap:
        Overlap_Numbers.write(str(number)+ ", ")
