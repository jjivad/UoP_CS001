# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:28:50 2019

@author: VIJ Global
"""

def sequence(n):
  while n != 1:
    print(n)
    if n % 2 == 0: # n is even
      n = n / 2
    else: # n is odd
      n = n*3 + 1

#sequence(5)

#while True:
#  line = input('> ')
#  if line == 'done':
#    break
#  print(line)
#print('Done!')

#a = 4
#x = 8
#while True:
#  print(x)
#  y = (x + a/x) / 2
#  if y == x:
#    break
#  x = y
#  
#strings
gtgs = "Hello World"
#print(gtgs[7])

def find(word, letter):
  index = 0
  while index < len(word):
    print(index)
    if word[index] == letter:
      return word[index]
    index = index + 1
  return -1 

#print(find("Jessy Inga", "a"))

#forum example, dealing with strings  
#question 1
def any_lowercase1(s):
  for c in s:
    if c.islower():
      print(c, "lower letter")
      return True
    else:
      print(c, "upper letter")
      return False    
#word = "JessyIngacare"
#print(any_lowercase1(word))

#question 2 
def any_lowercase2(s):
  for c in s:
    print(c)
    if 'c'.islower():
      print("lower letter")
      return 'True'
    else:
      print(c, "upper letter")
      return 'False' 
#  return True
#word = "JessyIngacare"
#print(any_lowercase2(word)) 
      
#question 3
def any_lowercase3(s):
  for c in s:
    print(c)
    flag = c.islower()
  return flag
#word = "JessyIngacare"
#print(any_lowercase3(word))  

def any_lowercase4(s):
  flag = False
  for c in s:
    print(c)
    flag = flag or c.islower()
  return flag
#word = "JessyIngacare"
#print(any_lowercase4(word)) 

def any_lowercase5(s):
  for c in s:
    print(c)
    if not c.islower():
      return False
  return True 
word = "jessyIngacare"
print(any_lowercase5(word))  
  
  
  
  
  
  
  
  