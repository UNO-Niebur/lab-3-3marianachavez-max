#ApproxPi.py
#Name: Mariana Chavez
#Date: 02.05.2026
#Assignment: Lab 3 Extra Credit
#Purpose: practice with boolean logic, conditional statements, loops (for and while), program flow control

import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  inputPercision = int(input("Enter the number of decimal places (up to 10) for the approximation of pi: ")) 
  while inputPercision < 0 or inputPercision > 10:
    inputPercision = int(input("Please enter a number between 0 and 10: "))
  
  start = time.time()
  #calculate pi using the approximation technique

  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denominator = 3
  while round(approxPi, inputPercision) != round(realPi, inputPercision):
    approxPi = approxPi + (sign * 4 / denominator)
    sign = sign * -1
    denominator = denominator + 2


  print(f"Approximated Pi: {round(approxPi, inputPercision)}")
  print(f"Real Pi: {realPi}")  
  end = time.time()

  elapsedTime = end - start
  print("The elapsed time is:", elapsedTime, "seconds")

if __name__ == '__main__':
  main()
