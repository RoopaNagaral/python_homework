# Task 4
def make_hangman(secret_word):
    guesess = []
    
    def hangman_closure(letter):
        guesess.append(letter)
        
        displayed = ""
        for ch in secret_word:
            if ch in guesess:
                displayed += ch
            else:
                displayed += "_"
        
        print(displayed)
        
        return all(ch in guesess for ch in secret_word)
      
    return hangman_closure

secret_word = input("Enter secret word: ")
game1 = make_hangman(secret_word)

while True:
    guess = input("Enter guess letter: ")
    
    finished = game1(guess)
    
    if finished:
        print(True)
        break
        