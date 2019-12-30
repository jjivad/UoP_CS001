# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:31:50 2019

@author: VIJ Global
"""

#print 'Hello, World!'___ error message: syntaxError
#1/2
#type(1/2)
##print(01)____Error: SyntaxError: invalid token
#1/(2/3)

import turtle
import math
bob = turtle.Turtle()
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)

#for i in range(4):
#  bob.fd(100)
#  bob.lt(90)
  
#print(bob)
turtle.mainloop()
#
#for i in range(4):
#  print('Hello!')
  
def polygon(t, n, length):
  angle = 360 / n
  for i in range(n):
    t.fd(length)
    t.lt(angle)
polygon(bob, 7, 70)


def circle(t, r):
  circumference = 2 * math.pi * r
  n = 50
  length = circumference / n
  polygon(t, n, length)































