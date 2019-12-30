# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:08:36 2019

@author: VIJ Global
"""


#I'm creating a simple function that will print the about of the function and return the value of the parameters
def aboutMe(name, surname, country, hobby):
  print("This function will print a sentence about myself")
  print("My name is " + name + " " + surname + ", I live in " + country + ", and " + hobby)
  
#the following lines will declare variables and their values  
my_name = 'Jessy'
my_surname = 'Inga'
my_country = 'Kenya'
my_hobby = "I love technology"

#this line below will print out the function and put the variables as arguments
aboutMe(my_name, my_surname, my_country, my_hobby)

print('') #for spacing the output, don't really mind about this line

#this line below will print out the function and use the value directly
aboutMe('Steven', 'Hett', 'USA', 'I love football')

print('') #for spacing the output, don't really mind about this line

# this function will print out the function and use expression
b = 'Thelemah'
c = 'I love travelling'
aboutMe('Yishay' *2, b*2, 'Congo', c)


#calling my function using the local variable 'me', remove the comment if you want to see the error output
def aboutYou(name, surname, country, hobby):
  me = "My name is " + name + " " + surname + ", I live in " + country + ", and " + hobby
  print("This function will print a sentence about myself")
  print(me)
#print(me) #will produce NameError since it's not recognized outside the function. it's a local variable in the function aboutMe


#creating a function with a parameter that has a unique name 
#def aboutThem(jessy):
#  print("Inga" * 3)
#  
#print(jessy) #pritting the parameter, NameError when run
  
print('') #for spacing the output, don't really mind about this line

def aboutUs(a):
  total = a + 10
  print ("the total number is", total)
  
total = 20
aboutUs(total)
print(total)
  















