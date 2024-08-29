import random

def guess_the_number():
    # Select a random word from the given list
    word= ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'hello']
    secret_word = random.choice(word)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've selected a random word from the below list. Try to guess it!")
    print(word)

    while True:
            guess = (input("Enter your guess: "))
            attempts += 1

            if guess != secret_word:
                print("Incorrect, Try Again")
            else:
                print(f"Congratulations! You guessed the number {secret_word} in {attempts} attempts.")
                break
if __name__ == "__main__":
    guess_the_number()