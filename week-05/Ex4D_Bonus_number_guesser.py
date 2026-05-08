numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mixed_numbers = [4, 9, 2, 7, 1, 10, 5, 8, 3, 6]

secret_number = mixed_numbers[0]

guesses = []
guess_count = 0 

print("Guess a number between 1 and 10")

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    guesses.append(guess)
    guess_count += 1

    if guess < secret_number:
        print("Higher")

    elif guess > secret_number:
        print("Lower")

    else:
        print("Correct! You guessed the number!")

        if guess_count < 5:
            print("Awesome! You got it in less than 5 guesses!")

        print("Number of guesses:", guess_count)
        print("Your guesses were:", guesses)

        break