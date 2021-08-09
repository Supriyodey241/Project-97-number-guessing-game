import random
print("Number Guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess A Number (between 1 and 9):")

while chances < 5:

    guess = int(input("Enter Your Guess:-"))



    if guess == number:
        print("Congratulations You Have Won!!!")
        break

    elif guess < number:
        print("Your Guess Was Too Low: Guess A Number Higher Than", guess)

    else:
        print("Your Guess Was Too High: Guess A Number Smaller Than", guess)

    chances += 1

if not chances < 5:
    print("You Loose!!! The Number Was", number)            