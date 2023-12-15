tupleOne = ('name', 1.2, False, 2)

print(type(tupleOne))
# tuples are immutable
print(tupleOne[-1])

# let us create a list with different elements

listOne = ["me", 24, 65.6, [12, 5], (True, 12)]

print(listOne)

# we are splicing listOne elements
print(listOne[3:5])

# lets add element to this list 
listOne.extend(['pop', 10])
print(listOne)
# lets add element to this list by using append method
listOne.append(['xmas', "gift"])
print(listOne)

del(listOne[2])
print(listOne)

# how change string to lists 
print("christ mas".split())

# lets clone list
listTwo = listOne[:]
print("cloned list")
print(listTwo)
# this will refer to different location on our memory space
listTwo[0] = "teo"

print(listOne, listTwo)

fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits)