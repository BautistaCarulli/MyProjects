import random as rd

def guessing_game():
    word = ["sea", "dog", "cat", "own", "any"]  # 3 letters word
    secret_word = rd.choice(word)
    remaining_attemps = 5

    print("Welcome to 3 letters word!")
    print("Try to guess the word!")

    while attemps > 0:
        attemps = input("Insert (3 letters word):").lower()

        if attemps == secret_word:
            print("¡Congrats! ¡You have passed the game!")
            return
        else:
            remaining_attemps -= 1
            print("Fail.You have",remaining_attemps, "attemps.")

    print("¡Sorry! You have lost. The word was:", secret_word)

# main function
guessing_game()

