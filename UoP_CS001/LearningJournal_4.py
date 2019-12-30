# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:55:51 2019

@author: VIJ Global
"""

#first stage
def hypotenuse1(a, b):
  return 0.0

#print(hypotenuse1(3,4))

#second stage, the side of the triangle. we know the addition of each side square give us the hypotenuse square. means their squareroot will be our hypotenuse.
def hypotenuse2(a, b):
  side_one = a**2
  side_two = b**2
  print("side one square is: ", side_one)
  print("side two square is: ", side_two)
  return 0.0

#print(hypotenuse2(3,4))

# third stage, we do the sum of those sides
def hypotenuse3(a, b):
  side_one = a**2
  side_two = b**2
  sum_sides = side_one + side_two
  print("the sum of the sides square is: ", sum_sides)
  return 0.0

#print(hypotenuse3(3,4))

# fourth stage, the squareroot of our hypotenuse [(a**2) + (b**2) = (c**2)]
import math #did import math to avoid the warning sign in my codes saying undefined name math.
def hypotenuse(a, b):
  side_one = a**2
  side_two = b**2
  sum_sides = side_one + side_two
  hyp = math.sqrt(sum_sides)
  print("the sum of the sides square is: ", sum_sides) # just for testing the sum of those sides square 
  return hyp

#print(hypotenuse(3,4))
#print(hypotenuse(5,7))
#print(hypotenuse(20,4))


#stage one, build the function
def salary_annual1(a, b, c):
  return 0.0
name= "Yishay"
salary_monthly = 5000
tax_monthly = 16
#print(salary_annual1(name, salary_monthly, tax_monthly))

#stage two, compute monthly net income.
def salary_annual2(a, b, c):
  tax_amount = b * (c/100)
  net_income = b - tax_amount
  print("your name is: ", a)
  print("your monthtly salary is: ", b)
  print("your monthly tax is: ", tax_amount)
  print("your net income is: ", net_income)
  return 0.0
name= "Yishay"
salary_monthly = 5000
tax_monthly = 16
#print(salary_annual2(name, salary_monthly, tax_monthly))

# stage three, have the annual salary net income

def salary_annual(a, b, c):
  tax_amount = b * (c/100)
  net_income = b - tax_amount
  annual_net_income = net_income * 12
  print("Hello ", a, ", after paying your tax monthly of ", tax_amount,", with ", net_income, " as monthly net income, you will get the below amount every year:")
  return annual_net_income
name= "Yishay"
salary_monthly = 5000
tax_monthly = 16
#print(salary_annual(name, salary_monthly, tax_monthly))

nam = "Inga"
salary = 20000
tax = 5
print(salary_annual(nam, salary, tax))
print (salary_annual("Jessy", 100000, 6))
print(salary_annual("Dan", 7000, 2))








