#RPS.py
#Name: Mariana Chavez 
#Date: 02.05.2026
#Assignment: Lab 3
#Purpose: practice with boolean logic, conditional statements, loops (for and while), program flow control

#COMMENT: I added strip().upper() so lowercase could be used as well, otherwise even if the player would win
#it would count as a loss.
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  playAgain = "Y"
  while playAgain == "Y":

    print("Welcome to Rock, Paper, Scissors! Rock=R, Paper=P, Scissors=S")

    computer = random.choice(['R', 'P', 'S'])
    player = input("Enter your choice(R, P, S): ").strip().upper()

    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")
      
    if player == "R":
      print("You chose Rock")
    elif player == "P":
      print("You chose Paper")
    else:
      print("You chose Scissors")

    if player == "R" and computer == "R" or \
    player == "P" and computer == "P" or \
    player == "S" and computer == "S":
      print("It's a tie!")
      ties = ties + 1
    elif (player == "R" and computer == "S") or \
    (player == "P" and computer == "R") or \
    (player == "S" and computer == "P"):
      print("You win!")
      wins = wins + 1
    else:
      print("You lose!")
      losses = losses + 1

    playAgain = input("Do you want to play again? (Y/N): ").strip().upper()

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
