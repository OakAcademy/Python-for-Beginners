import random
import time

print("""

Number Game.
Guess the number between 1 and 100.
You have 7 attempts.
Let’s start.

""")

Random_Number = random.randint(1,100)
Attempt = 7
Counter = 0

while True:
    Guess = int(input("Enter your guess: "))

    if (Random_Number > Guess):
        print("Comparing numbers...")
        time.sleep(1)
        print("Your guess is lower than our number. Try again")
        Attempt -=1
        Counter +=1

    elif (Random_Number < Guess):
        print("Comparing numbers...")
        time.sleep(1)
        print("Your guess is higher than our number. Try again")
        Attempt -= 1
        Counter += 1
    else:
        print("Comparing numbers...")
        time.sleep(1)
        print("Congratulations. Right guess. Our number is: ", Random_Number)
        print("You guessed in", Counter, "attempt(s)" )
