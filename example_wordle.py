import random


def generate_word():
    word_list = ['apple', 'banana', 'orange', 'grape', 'pear']
    return random.choice(word_list)


def check_guess(word, guess):
    if len(guess) != len(word):
        return False

    for i in range(len(word)):
        if guess[i] != word[i] and guess[i] in word:
            return 'X'
        elif guess[i] == word[i]:
            return 'O'

    return False


def play_wordle():
    word = generate_word()
    attempts = 0

    while True:
        guess = input("Enter your guess: ").lower()

        if guess == word:
            print("Congratulations! You guessed the word correctly!")
            break

        result = check_guess(word, guess)

        if result:
            print(result, end=' ')

        attempts += 1
        if attempts >= 5:
            print("\nSorry, you have reached the maximum number of attempts.")
            print("The word was:", word)
            break


play_wordle()

