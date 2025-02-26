#WordCount.py
#Name: Luke Knofczynski
#Date: 2/26/25
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount += 1
    
    words = line.split()
    
    for word in words:
      wordCount += 1
      
      for letter in word:
        letterCount += 1
        
  print( "Lines: ", lineCount)
  print("words: ", wordCount)
  print("letters: ", letterCount)
if __name__ == '__main__':
  main()
