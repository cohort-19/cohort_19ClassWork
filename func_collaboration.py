#functions by default donot share anything from themselves
def add() :
    num1,num2 = 10,20
    return(num1+num2)
add()    

print(add())

def multiply() :
    num3,num4 = 30,2
    print(num3*num4)
multiply()

print(multiply())
num = multiply()
print (num)