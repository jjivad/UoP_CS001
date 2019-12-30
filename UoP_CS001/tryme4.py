# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:14:49 2019

@author: VIJ Global
"""
#this function prints a line with a dot
def new_line():
  print('.')

#this function calls the new_line function 3 times to print 3 lines    
def three_lines():
  new_line()
  new_line()
  new_line()


#this function calls the three_lines function 3 times to print 9 lines 
def nine_lines():
  three_lines()
  three_lines()
  three_lines()
print("calling the 9 lines") 
nine_lines()


# this function call all the 3 previous functions: nine_lines, three_lines and new_line to print a total of 13 lines
def clear_screen():
  nine_lines()
  three_lines()
  new_line()
  
#print("calling the 22 lines that combine nine_lines and clear_screen functions")  
#nine_lines(), clear_screen() 
#last line calling the nine_lines and clear_screen functions. but this gives 22 lines




print("if you need 25 lines, you need to include three_lines, nine_lines and clear_screen functions to your calling statement")
three_lines(), nine_lines(), clear_screen() # this gives 25 lines if we include the three_lines function.