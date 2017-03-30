Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).

word = open('words.txt')

wordCount = 0
lineCount = 0
for line in word:
   if len(line) >= 20:
      print line
      wordCount += 1
