#another way of writing classes
class Animal:
#function__ is a special method we use as a constructor
#the first parameter in that function is used to identify the property, attribute , or characteristic or feature of the class
    def __init__(self,name,habitat,age,color,youngone):
        self.name = name
        self.habitat = habitat
        self.age = age
        self.color = color
        self.youngone = youngone

animal1 = Animal("lion", "Den", 19, "Brown", "Cub")
#create 5 classes in this with atleast 5 properties in a dynamic way


class Car:
     def __init__(self,name,type,color,milage,size):
        self.name = name
        self.type = type
        self.color = color
        self.milage = milage
        self.size = size

animal1 = Car("Toyota", "Double cabin", "blue", 195, "big")