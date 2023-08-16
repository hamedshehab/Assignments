#حامد شهاب الصبري


import random

print("Welcome to hangman")
print("-------------------------------------------")

wordDictionary = ["fire", "house", "cloud", "city","ronaldo","messi", "teacher", "game", "movie"]

### Choose a random word
randomWord = random.choice(wordDictionary) 



for x in randomWord:
  print("_", end=" ")

def print_tries():
    global n
    print(f"You have {amount_of_times_wrong} tries")

def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 10
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 0 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  print("\n\n\n**************************************")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(randomWord[current_guess_index] == letterGuessed):
    print_tries()
    ### Print word
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong
  else:
    amount_of_times_wrong-=1
    current_letters_guessed.append(letterGuessed)
    ### Update the tries
    print_tries()
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

print(f"\nGame is over! The word was {randomWord}")