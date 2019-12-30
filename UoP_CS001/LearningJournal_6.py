# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:02:12 2019

@author: VIJ Global
"""
# Part one
my_variable = 'Yishay Inga Volonte Jessy Thelemah' # string variable creation
my_variable_list = my_variable.split() #list creation from the string variable, spliting it.
print("The initial list = ", my_variable_list)

pop_element = my_variable_list.pop(2) # using pop to delement the 3 element in this list
print("The pop elemet is = ", pop_element) #to check which element was deleted
print("The list after pop = ", my_variable_list) #to see the current list

del my_variable_list[1] # using del operator
print("The list after del = ", my_variable_list) # to see the current list

my_variable_list.remove('Thelemah') # using remove, if I know the element that I want to delete from the list.
print("The list after remove = ", my_variable_list) #to see the current list

my_variable_list.sort() # here I've done the sorting
print(my_variable_list)

my_variable_list.append('Loulou') #adding an element to the list with append
print(my_variable_list)

g = ['Nounou', 'Coucou']
my_variable_list.extend(g) #just added element that belong to g to m list: my_variable_list
print(my_variable_list)

my_variable_list.insert(1, "Joujou") # I've inserted an element between the first and the second elements. 'Yishay' that was on index 1, now it's on index 2 because the insert has pushed it.
print(my_variable_list)

join_sign = ' ' # help to join the elemets with space between them
my_variable_list_joined = join_sign.join(my_variable_list)
print(my_variable_list_joined) # to see our final string after all the modifications


# Part 2

my_nested_list = [5, 8, 15, [20, 32, 35, 41], 43, 50] # the nested list: list inside a list
list_mult = my_nested_list * 2 # using * operator. it will double the first list
print(list_mult)
first_slice = my_nested_list[:3] # specifying the end
second_slice = my_nested_list[2:] # specifying the beginning
third_slice = my_nested_list[1:3] # specifying the end and the beginning
print(first_slice)
print(second_slice)
print(third_slice)

list_add = [0, 1]
list_add += my_nested_list # use of the += operator to add up 2 lists
print(list_add)

filter_list = []
for i in list_add: # this loop will help to filter the element we want by following the set down (in the body)
  if type(i) != int:
    filter_list.append('not int')
  elif i % 5 == 0:
    filter_list.append(i)
    print(filter_list)

def del_element(li):
  li = li.sort() #wrong since it will not return a sorted list but None
  
print(del_element(first_slice))
print(first_slice)


# Part 3
#About peer assessment, it's fine. I like the feedbacks and contributions that other students are providing. just it feel ackward sometime to see the grades that you know you've done good but someone deny it... and we have to accept it like that!



















































