from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
# print(f"Pssst, the solution is {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word is {chosen_word}")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])