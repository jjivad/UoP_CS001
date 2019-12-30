# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:40:56 2019

@author: VIJ Global
"""

#def area(l,w):
#  temp = l*w;
#  return temp
#
#l = 4.0
#w = 3.25
#x = area(l, w)
#if (x):
#  print(x)
#  
#def a(le, wi, he):
#  print("the area of the box is ", le*wi*he)
#  return le*wi*he
#l = 12.5
#w = 5
#h = 2
#a(l,w,h)
#print("the area of the box is ", le*wi*he)

#def f2(pa):
#  print(pa,pa)
#  #print(cat)
#  
#def f1(p1, p2):
#  cat = p1 + p2
#  f2(cat)
#ch1 = "see you "
#ch2 = "see me "
#f1(ch1, ch2)

#n = int(10.)
#print(n)
#print(isinstance(n, float), isinstance(n * 1.0, float))

#def test_fun(l, w, h):
#  print("the area of the box is ", l*w*h)
#  return l*w*h
#
#l = 12.5
#w = 5
#h = 2
#test_fun(l, w, h)

#def square_area(n, m):
#  my_area = n * m
#  #return my_area
#  return cat
#num1 = "Jessy"
#num2 = "Inga"
#num3 = 5
#num4 = 4
#square_area(num1, num2) #string instead of integer
#square_area(num3)
#
#def square_area(n, m):
#	my_area = n * m 
#	if my_area > 0: # here the identation
#	return my_area
#	if my_area < 0:
#	return 0
#num3 = 5
#num4 = 4
#square_area(num3, num4)

#def value_area(n, m):
#	my_area = n * m # here it should be n*m to have that area
#	return my_area # will return a value different from the real value we want to see
#num3 = 5
#num4 = 4
#print(value_area(num3, num4))

#def value_area(n, m):
#	my_area = n * m 
#	return cat # an error will be produced since that variable is not anywhere in the function, not recognized.
#num3 = 5
#num4 = 4
#print(value_area(num3, num4))

def is_divisible(x, y):
  if x % y == 0:
    return True
  else:
    return False
  
#def is_power(a, b):
#  if is_divisible(a, b) and is_divisible(a/b, b):
#    return True
#  else:
#    return False

#num1 = 10
#num2 = 1
#print(is_divisible(num1, num2))
#print(is_power1(num1, num2))

#print("is_power(10, 2) returns: ", is_power(10, 2))
#print("is_power(27, 3) returns: ", is_power(27, 3))
#print("is_power(1, 1) returns: ", is_power(1, 1))
#print("is_power(10, 1) returns: ", is_power(10, 1))
#print("is_power(3, 3) returns: ", is_power(3, 3))
  
#
def is_power(a, b):
  print("value of a: ", a , " value of b: ", b)
  if a/b == 1:
    return True
  elif is_divisible(a, b) and is_power(a/b, b):
    return True
  else:
    return False

print("is_power(10, 2) returns: ", is_power(10, 2))
#print("is_power(27, 3) returns: ", is_power(27, 3))
#print("is_power(1, 1) returns: ", is_power(1, 1))
#print("is_power(10, 1) returns: ", is_power(10, 1))
#print("is_power(3, 3) returns: ", is_power(3, 3))

























