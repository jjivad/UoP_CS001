# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:26:47 2019

@author: VIJ Global
"""

# the function below is for positive number recursive, counting down
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)
    
# the function below is for negative number recursive, counting up
def countup(n):
  if n >= 0:
    print("C'est fini!")
  else:
    print(n)
    countup(n+1)
    
countdown(3)
print('')
countup(-3)

# asking for an input so that the user can enter any number of her/his choice
n = int(input("please enter a number: "))

if n == 0:  # if the provided number is equal to 0, it will provide both functions: countdown and countup.
  countdown(n)
  countup(n)
  
elif n > 0:  # if the provided number is positive
  countdown(n)
  
elif n < 0:  # is the provided number is negative
  countup(n)
  

# my runTimeError when there is an infinite recursion
def Error_Try(n):  
  if n <= 0:
    print("woiiiiiii!!!")
  else:
    
    Error_Try(n-1)
    
Error_Try(6)    
      
    
    
    
    