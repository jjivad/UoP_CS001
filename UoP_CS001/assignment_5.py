# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:04:55 2019

@author: VIJ Global
"""
#encapsulation of the square-root codes, part 1
def my_sqrt(a):
  x = 3
  while True:
     y = (x + a/x) / 2.0
     if y == x:
          break
     x = y
  return y

#num_square = 16
#print(my_sqrt(num_square))

# square root table, part 2
import math
def test_sqrt(n):
  a = 1
  while a <= n:
    print("a= ", a, "| my_sqrt(", a, ") = ", my_sqrt(a), " | math.sqrt(", a, ") = ", math.sqrt(a), " | diff = ", abs(my_sqrt(a) - math.sqrt(a)))
    a += 1
    
test_sqrt(25) # I just use 25 as an argument (requested by the instructor). you can replace it with any number to have the output you need.   
     
#the print statement contain the call of the previous function my_sqrt, contain the call of the real math square-root function, then give the absolute value of the difference of the 2 functions.     
     
     

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     