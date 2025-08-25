import random

low=1
high=9
guesses=0
number=random.randint(low,high)

while True:
    guess = int(input(f"Guess a number between ({low}-{high}):"))

    guesses+=1



    if guess < number:
        print("The number is low")

    elif guess > number:
        print("The number is high")

    else:
        print("The number is right")
        break

print(f"This round took you {guesses} guesses to complete successfully")