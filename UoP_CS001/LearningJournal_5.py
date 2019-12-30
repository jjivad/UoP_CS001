# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:32:34 2019

@author: VIJ Global
"""
#question 1
prefixes = 'JKLMNOPQ'
suffix = 'ack'
# first loop before change
for letter in prefixes:
     print(letter + suffix)
 
print(" ") #tp separate the output
  
for letter in prefixes:
  if letter == "O":
    print(letter + "u" + suffix)
  elif letter == "Q":
    print(letter + "u" + suffix)
  else:
    print(letter + suffix)

print(" ")
#question 2

names = "Jessy Inga"
beginning = names[:5] # first slice where the output will display the beginning of the word. Here I wanted to show that you can tell where to stop whithout specifying the beginning.
middle = names[3:8] #second slice where the output will display the middle part. but the goal of this slice is showing that you can give it a beginning and the end. where to start and where to end

end = names[6:] #with this slice, we give it where to start but no ending. the code will detect automatically where to stop

print(beginning)
print(middle)
print(end)


print(" ")

print("bib".find('b', 1, 2)) #question 1 self quiz

print("")

while True: #question 2

    while 1 > 0:

        break

    print("Got it!")

    break

print("")

print("Xanadu" > "Yellowstone") #question 3

print("")

n = 10000  #question 4
count = 0
while n:
    count = count + 1
    n = n // 10
print (count)

print("")

#fred = "Hello" #question 10
#fred[0] = "Y"




