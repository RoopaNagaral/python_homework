# Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())

        # Build the displayed word EXACTLY like the assignment example
        displayed = ""
        for ch in secret_word.lower():
            if ch in guesses:
                displayed += ch
            else:
                displayed += "_"

        print(displayed)

        # Return True only when all letters have been guessed
        return all(ch in guesses for ch in secret_word.lower())

    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip()
    hangman = make_hangman(secret)

    print("Start guessing letters!")

    # Keep prompting until the full word is guessed
    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            continue

        done = hangman(guess)
        if done:
            print("You guessed the word!")
            break

# --- Task Completed ---