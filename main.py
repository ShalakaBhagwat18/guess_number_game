#importing logo
from guess_logo import logo
print(logo)
import random
EASY_LEVEL=10
HARD_LEVEL=5
#creating function to check user's guess against actual answer.
def check_answer(guess,answer,turns):
  if guess>answer:
    print("Too high") 
    return turns-1
  elif guess<answer:
    print("Too low")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}.")
def set_difficulty():
  level=input("\nChoose a difficulty. Type 'easy' or 'hard':")
  if level=="easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
    
def game(): 
  """Fuction for check guess with answer. Return the number of terns remaining. """
  #choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer=random.randint(1,100)
  print(f"{answer} Pass the computer to a player")
  
  #ask user to make a guess
  
  turns=set_difficulty()
 
  #repeat the guessing fuctionallity utile all the attempts are over
  guess=0
  while guess !=answer:
    print(f"You have {turns} attempts remaing to guess the number")
    guess=int(input("Make a guess:"))
    turns=check_answer(guess,answer,turns)
    if turns==0:
      print("You've run out of guesses, you lose.")
      break
    elif guess!=answer:
      print("Guess again.")
    
    
#track to decrease the number of turns by 1 if they get it wrong
game()    
