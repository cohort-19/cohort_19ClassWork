def even_number():
    for number in range(10):
       if number %2 != 1:
           print(number)
even_number()

def sum():
    num1, num2 = 10, 20
    num3 = num1 + num2
    print(num3)
sum()

#arithmetic operators
def add(a, b):
    print("The sum is:", a + b)
add(4,2)

def subtract(a, b):
    print("The difference is:", a - b)
subtract(4,2)

def multiply(a, b):
    print("The product is:", a * b)
multiply(4,2)

def divide(a, b):
    print("The quotient is:", a / b)
divide(4,2)

def remainder_after_division(a, b):
    print("The remainder is:", a % b)
remainder_after_division(4,2)

def power(a, b):
    print("The power is:", a ** b)
power(4,2)