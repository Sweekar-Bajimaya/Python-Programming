import random
print("Welcome! to the Hangman Game")
print("Lets get Started")
# List of words to choose from
words = ["python", "programming", "computer", "science", "coding"]
# Randomly choose a word from the list
word = random.choice(words)
# Create a list of underscores the same length as the word
guessed_word = ["_"] * len(word)
# Number of allowed guesses
guesses = 6
# Keep track of previously guessed letters
guessed_letters = []
while "_" in guessed_word and guesses > 0:
    # Print the current status of the guessed word
    print(" ".join(guessed_word))
    print("Guesses remaining: ", guesses)
    print("Guessed letters: ", guessed_letters)
    # Get input from the user
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
    elif letter in word:
        # Update the guessed word with the new letter
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
    else:
        print("Incorrect. The letter is not in the word.")
        guesses -= 1
        guessed_letters.append(letter)
if "_" not in guessed_word:
    print("Congratulations! You guessed the word: ", word)
else:
    print("Sorry, you ran out of guesses. The word was ", word)
