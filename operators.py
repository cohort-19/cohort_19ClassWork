#arithmeticoperators
num1, num2 = 20, 30
print(num1 + num2)
print(num2 - num1)
print(num1 * num2)
print(num2 / num1)
print(num2 // num1)
print(num1 ** num2)
print(num1 % 2)
print(2 % num1)



#assignment operators
my_num = 200
#+=
num3 = 10 # this means num3=num3+5
num3 += 5
print(num3)


#comparison operator
print(10 == 10)
print(10 == "10")
print(10 < 10)
print(10 > 8)
print(10 <= 10)
print(10 >= 10)
print(10 != 10)

#logical operators
#logical and
num4 = 5
num5 = 6
print ((num4>2) and (num5>=6))
print ((num4>2) and (num5>=8))

#logical or
print ((num4>2) or (num5>=6))
print ((num4>2) or (num5>=8))

#logical not
print (not True)
print (not False)

#bitwise operators
#special operators(identity and membership)
#identity
#is and is not
print(True is True)
print(True is not True)
print(True is not False)
print(False is not False)
 
#membership
#in and not in
my_nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(10 in my_nums)
print(10 not in my_nums)
name = "Janet"
print("m" in name)
