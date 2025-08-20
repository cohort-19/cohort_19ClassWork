#class methods
#this is a function in a class
class Woman():
    name = "Maria"
    age = 23
    color = "brown"
    def cook():
        return f"{Woman.name} cooks nicely!"
        return(self.name,"cooks nicely")
    
    #a method is a function of a class that describes what an object does to itself or others.
    # a method describes the behaviour of a class
    # statement with in a line of a method is a behaviour
    #a behaviour describes how an object does soething/acts
    #any other statements below return are ignores or considered as coments
print(Woman.cook())


woman2 = Woman()
woman2.name = "Norah"
woman2.age = 44
woman2.color = "brown"
#print(woman2.cook())
#this statement will result into an error because cook only takes 0 positional arguments and it has already been taken by Maria

