import random  # Import random module

# Generate a random number between 1 and 10
target = random.randint(1, 10)

# Keep asking the user until they guess correctly
while True:
    guess = int(input("Guess the number: "))  # Get user input
    if guess == target:
        print("Correct! 🎉")
        break  # Exit the loop if the guess is correct
    else:
        print("Wrong, try again!")
