import random as rand
from stages import stages, logo
from hangman_words import word_list

word = rand.choice(word_list)
blanks = len(word) * "_"
lives = 6
game_over = False

print(logo)

while not game_over:
    print(blanks)
    print(stages[lives])
    shot = input("Guess a letter: ").lower()
    if shot not in word:
        lives -= 1
        print(f"Letter {shot} is not in a word.\n")
        if lives == 0:
            print(stages[lives])
            print("GAME OVER")
            game_over = True
    else:
        if shot in blanks:
            lives -= 1
            print(f"Letter {shot} was already guessed.")
            if lives == 0:
                print(stages[lives])
                print("GAME OVER")
                game_over = True
        else:
            blanks = list(blanks)
            for i in range(len(word)):
                if word[i] == shot:
                    blanks[i] = shot

            blanks = "".join(blanks)
            if "_" not in blanks:
                print(f"You've won! The word was: {blanks}")
                game_over = True
