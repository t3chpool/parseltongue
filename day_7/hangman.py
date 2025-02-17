import random
import hangman_words
from hangman_art import stages
from hangman_logo import logo


# Pick a word from the provided list
lives = 6

print(logo)

chosen_word = random.choice(hangman_words.word_list)

# Print 'underscores' as replacement of chosen word.
placeholder = ""
for x in chosen_word:
    placeholder += "_"
print(placeholder)    


# Let user guess again
game_over = False
correct_letters = []

while not game_over:
    # Ask user to guess a letter from the word
    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Guess a letter from the word: ").lower()

    # Check if user has already guessed the letter
    if guess in correct_letters:
        print(f"You have already guess letter \"{guess}\"")

    # Check if the letter guessed by user matches letter in the word.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed letter \"{guess}\", which is not in the word. You loose a life.")
        if lives == 0:
            game_over = True
            print(f"You Loose. Correct word was \"{chosen_word}\"")
        
    
    if "_" not in display:
        game_over = True
        print("You Win !!!")
        
    print(stages[lives])
