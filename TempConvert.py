#TempConvert.py
#Name: Mariana Chavez
#Date: 02.05.2026
#Assignment: Lab 3
#Purpose: practice with boolean logic, conditional statements, loops (for and while), program flow control



def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("Enter a temperature in Fahrenheit: "))
  
  tempC = (tempF - 32) * 5/9

  print(tempF, "Fahrenheit is ", round(tempC, 1), "degrees celsius.")
if __name__ == '__main__':
  main()
