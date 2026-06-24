import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Enter a number (1-100): "))

    if guess == secret:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")