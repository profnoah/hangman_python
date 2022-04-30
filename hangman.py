import random
import string
from words import words
from graphic import lives_dict


def get_word():
    word = random.choice(words)
    return word.upper()


def hangman():
    word = get_word()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 7

    while lives > 0:
        # word_list = []
        # for letter in word:
        #    if letter in used_letters:
        #       word_list.append(letter)
        #    else:
        #       word_list.append("-")
        word_list = [letter if letter in used_letters else "-" for letter in word]

        print(lives_dict[lives])
        print("Current Word:", " ".join(word_list))

        user_letter = input("Guess a letter:").upper()

        if user_letter in used_letters:
            print("\n You entered same letter. Guess another one")
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("\n Your letter ", user_letter, " is not in the word")
        else:
            print("\n Invalid Chracter entered")

    if lives == 0:
        print(lives_dict[lives])
        print("\n You Died, The Word was", word)
    else:
        print("Congrats, you guessed the word", word)


hangman()
