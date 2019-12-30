# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:01:13 2019

@author: VIJ Global
"""

t = ['a', 'd', 'c', 'b', 'e', 'f']
t.append('z')
#print(t)

t.sort()
#print(t)

def addup(t):
  total = 0
  for i in t:
    total += i
  return total

numbers = [20, 10, 5, 50, 70, 5, 86]
#print(addup(numbers))
  
def capitalize_all(t):
  res = []
  for s in t:
    res.append(s.capitalize())
  return res

#print(capitalize_all(t))


def only_upper(t):
  res = []
  for s in t:
    if s.isupper():
      res.append(s)
  return res

our_list = ['l', 'JESSY', 'kid', 'Li', 'ME']
#print(only_upper(our_list))

list_initial = ['ami', 'hurt', 'love', 'friend', 'fire', 'cold', 'sad']
list_pop = list_initial.pop(1)
#print(list_pop)
#print(list_initial)

list_initial.remove('sad')
#print(list_initial)

del list_initial[3]
#print(list_initial)

name = 'JessyInga'
name_list = list(name)
#print(name_list)

name2 = 'Jessy Inga Volonte'
name_split = name2.split()
#print(name_split)

s ='spam-spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
#print(t)

t_list = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
join_list = delimiter.join(t_list)
#print(join_list)

a = 'jessy'
b = 'jessy'
#print(a is b) #verify

c = [1,2,3,4]
d = [1,2,3,4]
#print(c is d) #doesn't verify

e = 3
f = 3
#print(e is f) #verify

v = 8.9
w = 8.9
#print(v is w)

# objects and values: when coding, we assign objects to variables. when those objects are evaluated, we get the values. objects can be equivalent but not necessarily identical. but if the objects are identical they are equivalent.

#identical objects, also equivalent:
# equivalent objects, but not identical:
names_one = ['jessy', 'inga', 'volonte', 'yishay', 'thelemah']
names_two = ['jessy', 'inga', 'volonte', 'yishay', 'thelemah']
#print(names_one is names_two)
#to see the value output:
sep = ' '
t1 = sep.join(names_one)
t2 = sep.join(names_two)
#print('names_one = ', t1)
#print('names_two = ', t2)
#print(names_one)
#print(names_two)
# if you look at this output above, the names are the same... by printing those 2 lists you will have the same values, but this doesn't make them identical; they are just equivalent.

# objects, references, and aliasing
# objects are assign to variables. when a variable is assign to another variable, this last will take the object of the first one. This is aliasing. Aliasing happens when an object has more than one  reference, then it becomes aliased.

# reference, above when I was saying that objects are assigned to variables. the good term is reference. "The association of a variable with an object is called a reference" (Downey, 2015, p. 96)
Tut_family_names = ['Deng', 'Gak', 'Puok', 'Gatdet']
Anne_family_names = Tut_family_names
#print(Anne_family_names is Tut_family_names)
# here Anne family names will have also the same names like Tutus, this will make those two variables identical and equivalent.
#the list ['Deng', 'Gak', 'Puok', 'Gatdet'] has been refered to Tut_family_names. and because Tut_family_names is assigned to Anne_family_names, this make this list ['Deng', 'Gak', 'Puok', 'Gatdet'] to be aliased.


#reference:
#Downey, A. (2015). Think Python, How to think like a computer scientist. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)

def objects_try(t): # t here is a parameter
  equivalent_object = []
  identical_object = []
  for i in range (len(t)): #this loop will create an equivalent object to the first list by passing the same values on this new list: equivalent_object.
    equivalent_object.append(t[i])
    print(equivalent_object)
#    print("")
  print("testing equivalent objects: ", equivalent_object is t)
  if t != []: #this condition is going to create an identical object to the first list in case the first list is not empty. and it will make the object to be aliased because if it will be assigned to more that 2 variable: t and identical_object
    identical_object = t
    print("testing identical objects: ", identical_object is t)
  print("")
  return equivalent_object, identical_object 

my_list = [12, 'jessy', 9.0] # here you can see the reference, the association of [12, 'jessy', 9.0] with my_list.

#print(objects_try(my_list)) # my_list is ann argument passed to the objects_try function.

#index = "Ability is a poor man's wealth".find("w")
#print(index)

#my_list1 = [3, 2, 1]
#print(my_list1)

mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
total = 0
while a < 3:
    b = 0
    while b < 2:
        total += mylist[a][b]
        b += 1
    a += 1
#print(total)

#my_list = [3, 2, 1]
#print(my_list.sort())
    
def print_n(s, n):
     if n > 0:
          print(s)
          print_n(s, n-1)
     return n
n = 3
#while print_n("hi", n):
#     print_n("there!", n)
#     n = 0


n = 10
#while n != 1:
#    print(n,)
#    if n % 2 == 0: # n is even
#        n = n / 2
#    else: # n is odd
#        n = n * 3 + 1  
  
#pi = int(3.14159)
#print (pi)  
  
s = "help"
for letter in s[1:]:
      last = letter
      break
#print(last) 

bruce = 5
#print (bruce,)
bruce = 7
#print (bruce)

def function2(param):
    print (param, param)
def function1(part1, part2):
    cat = part1 + part2
    function2(cat)
chant1 = "See You "
chant2 = "See Me "
#function1(chant1, chant2)

percentage = float ( 60 * 100) / 55
#print (percentage)  

x = 5
#if x % 2 == 0:
#    print (x)
#else:
#    print (x, x%2)

#if "Ni!":
#    print ('We are the Knights who say, "Ni!"')
#else:
#    print ("Stop it! No more of this!")

#def area(l, w):
#    temp = l * w
#    return temp
#l = 4.0
#w = 3.25
#x = area(l, w)
#if ( x ):
#    print (x)

def is_divisible(x, y):
    return (x % y) == 0
x = 10
y = 1
#print(is_divisible(x, y))

#print('Unit 6'[-1])

n = 2
n += 5
n

pi = float(3.14159)
#print (pi)


def subroutine(n):
    while n > 0:
        print (n,)
        n -= 1
  
num = 5
subroutine(num)  
  
  