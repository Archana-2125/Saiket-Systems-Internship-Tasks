import random

number = random.randint(1, 100)

for attempts in range(1, 8):
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        print(f"You guessed it in {attempts} attempts.")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

else:
    print("Game over!")
    print("The correct number was", number)