'''
This is the first python project in my journey of learning python in detail.This project was initiated on 16 August,2025. In this project, I learned to run system commands with the help of sys and subprocess module. Also, I learned abouta module called wonderwords that helped me to get the random words of a specified length which was used in this game to give the guessing word to the user. Finally, in this project I used time module to display the time elapsed on playing the game.
'''

#Ensuring module is installed on machine
import sys
import subprocess
import time

try:
    from wonderwords import RandomWord
except ImportError:
    print('Importing Required Libraries')
    subprocess.check_call([sys.executable,'-m','pip','install','wonderwords'])
    from wonderwords import RandomWord


r = RandomWord()
word = r.word(word_min_length=8,word_max_length=16)
guessed = ['_']*len(word)
used_letters = []
attempts = 6

#To greet the user
print("Welcome to my Hangman Game.")
print("Guess the word:")
# print(word)
start_time = time.time()

while attempts > 0 and ('_'  in guessed):
    print("Word: "," ".join(guessed))
    print(f"Attempts left: {attempts}")
    print(f"Remaining Fields: {guessed.count('_')}\n")
    print(f"Used letters: {",".join(used_letters)}")
    guess = input("Enter guess letter: ").lower()
    if not guess.isalpha() or len(guess)!=1:
        print("⚠️ Only single letter allowed")
        continue
    if guess in used_letters:
        print("⚠️ The letter is already guessed.")
        continue

    used_letters.append(guess)

    if guess not in word:
        print("Incorrect Guess ❌")
        attempts -=1
    else:
        print("Correct Guess ✅")
        for i,l in enumerate(word):
            if l == guess:
                guessed[i] = guess
    

if word == "".join(guessed):
    print(f"\nCongratulations 🎉, you correctly guessed the word {word}")
else:
    print(f"\nGame over 💀! The correct word was: {word}")
print(f"Time Elapsed: {int(time.time()-start_time)} seconds")