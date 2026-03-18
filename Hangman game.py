import random
from countries import countries  # Import a list of country names

# Dictionary storing hangman stages based on number of wrong guesses
status = {
    0: ("   ", "   ", "   "),
    1: (" O  ", "   ", "   "),
    2: (" O  ", " |  ", "   "),
    3: (" O  ", "/|  ", "   "),
    4: (" O  ", "/|\\", "   "),
    5: (" O  ", "/|\\", "/  "),
    6: (" O  ", "/|\\", "/ \\")
}

# Displays the current hangman figure
def display_man(wrong_guesses):
    for i in status[wrong_guesses]:
        print(i)

# Displays the current progress of the guessed word
def display_hint(hint):
    print(" ".join(hint))

# Displays the full correct answer at the end
def display_answer(answer):
    print(" ".join(answer))

def main():
    is_running = True
    wrong_guesses = 0

    # Randomly select a country and convert to lowercase
    answer = random.choice(countries).lower()

    # Create a list of underscores to represent unguessed letters
    hint = ["_"] * len(answer)

    # Keep track of already guessed letters
    guessed = set()

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter your guess: ").lower()

        # Validate input (must be a single alphabet letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        # Prevent duplicate guesses
        if guess in guessed:
            print("You already guessed this letter")
            continue

        guessed.add(guess)

        # If guess is correct, reveal letter positions
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            # Increase wrong guess count if incorrect
            wrong_guesses += 1

        # Check win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win")
            break

        # Check lose condition
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose")
            is_running = False
            break

# Ensures the game runs only when this file is executed directly
if __name__ == "__main__":
    main()