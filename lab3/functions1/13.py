import random

def guess_the_number():

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)

    for guesses_taken in range(1, 11):  
        print("Take a guess.")
        guess = int(input())

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break  

    if guess == secret_number:
        print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
    else:
        print(f"Unfortunately, you couldn't guess the number : {secret_number}.")

guess_the_number()