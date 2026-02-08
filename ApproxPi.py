#ApproxPi.py
#Name: Mariana Chavez
#Date: 02.05.2026
#Assignment: Lab 3
#Purpose: practice with boolean logic, conditional statements, loops (for and while), program flow control
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
