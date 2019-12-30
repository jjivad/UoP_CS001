# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:24:40 2019

@author: VIJ Global
"""

#this is the function of testing the remainder of 2 numbers
def is_divisible(x, y):
  if x % y == 0:
    return True
  else:
    return False
  
  
#this is my written function of power a of b.
def is_power(a, b):
  print("value of a: ", a , " value of b: ", b) #this line help to check the recrusion progress to see if it is happening inside the
  if a/b == 1: #this code condition show the value of a/b equal to 1. we can only have 1 if a == b.
    return True
  elif b == 1: #this code is for the base, if the base is 1 then the function is true to avoid the RecursionError 
    return True
  elif is_divisible(a, b) and is_power(a/b, b):
    return True
  else:
    return False

#print("is_power(10, 2) returns: ", is_power(10, 2))
#print('') #for spacing between output
#print("is_power(27, 3) returns: ", is_power(27, 3))
#print('') #for spacing between output
#print("is_power(1, 1) returns: ", is_power(1, 1))
#print('') #for spacing between output
#print("is_power(10, 1) returns: ", is_power(10, 1))
#print('') #for spacing between output
#print("is_power(3, 3) returns: ", is_power(3, 3))
#print("is_power(100, 5) returns: ", is_power(100, 5)) #this is my own example i include to test



#mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
#a=0
#while a < 8:
#    print(mylist[a],)
#    a = a + 2
    
mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))