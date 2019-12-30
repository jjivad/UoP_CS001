# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:35:03 2019

@author: VIJ Global
"""

# part 1, calculating the volume of a sphere
piValue = 3.1416
def sphereVolume(r):
  volume = (4/3)*(piValue * ((r)**3))
  print(volume)

radius_one = 5
radius_two = 3
radius_three = 10

print("the value below is for first radius when calling the function sphereVolume: ")
sphereVolume(radius_one)

print("the value below is for second radius when calling the function sphereVolume: ")
sphereVolume(radius_two)

print("the value below is for third radius when calling the function sphereVolume: ")
sphereVolume(radius_three)

print(" " ) # just for spacing  part one codes output from part two codes output 

# part 2, create a unique function from mind
def myContact(name, phone, email):
  print(name + " your phone number is " + phone + " and your email address is " + email)
  
my_name = "Jessy"
my_phone = "0716622842"
my_email = "jessyinga1@gmail.com"

myContact(my_name, my_phone, my_email)
myContact("Yishay", "0758212077", "jessyinga1@gmail.com")
myContact(my_name, "0758212077", my_email )

