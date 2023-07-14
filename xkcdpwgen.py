#!/usr/bin/env python3

import argparse, random

parser = argparse.ArgumentParser(description = "Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words", type = int, help = "include WORDS words in the password", default = 4)
parser.add_argument("-c", "--caps", type = int, help = "capitalize the first letter of random words", default = 0)
parser.add_argument("-n", "--numbers", type = int, help = "insert NUMBERS random numbers in the password", default = 0)
parser.add_argument("-s", "--symbols", type = int, help = "insert SYMBOLS random symbols in the password", default = 0)

arguments = parser.parse_args()

file = open("words.txt", "r")
wordList = file.readlines()
numbers = '0123456789'
symbols = '(~!@#$%^&*.:;).'

# creates a password with four words randomly picked from the text file
def createPassword():
   password = []
   for i in range(arguments.words):
      password.append(random.choice(wordList).strip('\n'))
   return password

def createCapsPassword(listofwords):
  count = arguments.caps
  while (count > 0):
    length = len(listofwords)
    choice = random.randint(0, length - 1)
    item = listofwords[choice][0]
    if (not item.isupper()):
       listofwords[choice] = listofwords[choice].capitalize()
       count = count - 1
  
  listofwords = "".join(listofwords)
  return listofwords

def createNumSymPassword(word, count, itemlist):
    while (count > 0):
      word = list(word)
      wordLength = len(word)
      index = random.randint(0, wordLength - 1)
      if (word[index] not in list(symbols) or word[index] not in list(numbers)):
        word.insert(index, random.choice(itemlist))
        count = count - 1

    passwordNumSym = "".join(word)
    return passwordNumSym 


words = createPassword()
words = createCapsPassword(words)
words = createNumSymPassword(words, arguments.numbers, numbers)
words = createNumSymPassword(words, arguments.symbols, symbols)
print(words)