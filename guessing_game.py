import random


def self_guess(x):
    """a function where user guesses the number"""
    random_number = random.randint(1, x)
    guess = 0
    #loop to narrow down guesses
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")
    print(f"That's Right!!! The number is {random_number}")


def computer_guess(y):
    """a function where computer guesses the number"""
    upper = y
    lower = 1
    feedback = ''
    guess = ''
    # loop to narrow down guesses
    while feedback != 'c':
        guess = random.randint(lower, upper)
        feedback = input(f"Is {guess} too high, low or correct?(enter: h/l/c)").lower().strip()
        if feedback == 'h':
            upper = guess - 1
        elif feedback == 'l':
            lower = guess + 1
    print(f'Yes! the computer guessed it! Number is {guess}')


print("Do you want to guess the number or should the computer guess your number?")
game = input("Enter 'c' for computer guessing or anything else for your guess").lower().strip()
upper_bound = int(input("Enter the highest number"))
# contionals to choose game mode
if game == 'c':
    computer_guess(upper_bound)
else:
    self_guess(upper_bound)
