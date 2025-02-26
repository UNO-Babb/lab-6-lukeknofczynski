#DiceRoll.py
#Name: Luke Knofczynski
#Date: 2/26/25
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numrolls = 100000
  for count in range (numrolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    rolls[total-2] = rolls[total-2] + 1


  #find the sum total of the two dice
  num = 2
  for r in rolls:
    percent = round(r/numrolls * 100, 1 )
    print(num, ":", r, percent)
    num = num + 1

  #print statictics for dice rolls


if __name__ == '__main__':
  main()
