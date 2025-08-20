#different types of data types
#numeric
#intger , float and complex
print(type(100))
print(type(100.0))
print(type("100"))
print(type(1+2j))
#string value in quotes "",'', ``
name, gender,country ="Janet", "Female", "Uganda"
print(type(name))



#sequence
#list, tuple, range
   #list is a correction of values stored in rectangle brackets separated by commas eg a list of countries.
my_Countries = ["Uganda","Kenya","Tanzania"]
fruits = ["kiwi","orange","mango"]
numbers =["1","2","3","4"]
my_stuff = [my_Countries, fruits,numbers]
print(my_stuff)
#values in a list are indexed starting from zero from left to right.
print(my_Countries[0])
print(fruits[1])
print(numbers)
print(my_stuff[2][3])
#another list
numeral = [10,[20,40,[60,80,[[100],[200]]]]]
print(numeral[1][2][2][1][0])

#tuple is identified by a pair of parenthesis()
numbers1 =(1,20,8,5)
print(numbers1[2])
print(range(10))

#mapping

#boolean
#set