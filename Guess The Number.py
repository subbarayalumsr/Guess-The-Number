import random

secret = random.randint(1, 10)
chances = 5

print("Guess the number between 1 and 10")
print("You have", chances, "chances!")

for i in range(chances):
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess == secret:
        print("Correct! You guessed the number in", i + 1, "tries.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    print("Remaining chances:", chances - i - 1)

else:
    print("Game Over! The number was", secret)
