animals = ["pigs", "horese", "dog","cat", "goat", "lion"]
animals.append("elephant")
print(animals)
animals.pop()
print(animals)
birds = []
birds.append("hen")
print(birds)
#a list is mutable
# the tuple is immutable eg
#numbers = ()
#numbers.append("one")
#print(numbers)


animals.insert(1,"lion")
print(animals)

#mapping
#dictionary/dict{}
student = {"name":"Janet", "age":25, "location": "Mukono"}
print(student["age"])
print(student.keys())
print(student.values())


# aset is an unordered collection of unique items and is identified by {}
student_ids = {112, 113, 114, 118, 116, 116, 115, 118}
print(student_ids)