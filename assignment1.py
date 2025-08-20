# Demonstrating Different Data Types using Functions

def demonstrate_numbers_sequence():
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
demonstrate_numbers_sequence()

def demonstrate_mapping():
    student = {"name":"Janet", "age":25, "location": "Mukono"}
    print(student["age"])
    print(student.keys())
    print(student.values())
demonstrate_mapping()

#setsS
def demonstrate_sets():
    student_ids = {112, 113, 114, 118, 116, 116, 115, 118}
    print(student_ids)
demonstrate_sets()

def demonstrate_boolean_none():
    # Boolean data type example
    is_sunny = True
    is_raining = False

    print("is_sunny:", is_sunny)
    print("is_raining:", is_raining)

    print("is_sunny and is_raining:", is_sunny and is_raining)
    print("is_sunny or is_raining:", is_sunny or is_raining)
    print("not is_sunny:", not is_sunny)
demonstrate_boolean_none()


