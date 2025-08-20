#if
#else 
#elif
num = 10
if num > 0:
    print(num)

if num < 0:
    print("hello world!")

animals = ["goats", "cats", "dog"]
if "cats" in animals:
    print("cats")

if "rabbits" in animals:
    print("rabbits")


#below we are inputting a value from the keyboard directly to the variable my_input
#NOTE: input() takes everything as a string by default
#int(input()) converts a value from a string to an input.

else:
    print("rabbits are not part of the animal list")

my_input = int(input("please input your number: "))
if my_input < 0:
    print("the number you input is negative")
else:
    print("the number you input is positive")

if my_input % 2 == 0:
    print("the number input is an even number")
else:
    print("the number is an odd number")