import random

def guess_number():
    num = random.randint(1,100)
    n = 0
    high = 100
    low = 1
    while True:
        n = int(input(f"Guess a number between {low} and {high}: "))
        if n < num:
            print("higher! Try again.")
            low = n + 1
        elif n > num:
            print("lower! Try again.")
            high = n - 1
        else:
            print("Congratulations! You guessed the number.")
            break
guess_number()