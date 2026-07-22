def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        # Record the guess
        guesses.append(letter.lower())

        # Build the displayed word with underscores for unguessed letters
        revealed = ""
        for ch in secret_word.lower():
            if ch in guesses:
                revealed += ch
            else:
                revealed += "_"

        print(revealed)

        # Return True only when all letters have been guessed
        return all(ch in guesses for ch in secret_word.lower())

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip()
    hangman = make_hangman(secret_word)

    print("Start guessing letters!")

    # Keep prompting until the full word is guessed
    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        done = hangman(guess)
        if done:
            print("You guessed the word!")
            break

# --- Task Completed ---