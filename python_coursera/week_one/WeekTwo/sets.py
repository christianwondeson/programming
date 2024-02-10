# let us understand sets in python
setPL = {"Liverpool", "Man city", "Arsenal", "Aston Villa", "West Ham", "Arsenal"}
print(setPL)

# converting list into set (set Operations)
listToSetPL = set(
    ["java", "javascript", "python", "c", "c++", "c#", "ruby on rails", "java", "c"]
)
print(listToSetPL)

listToSetPL.add("GoLong")
print("updated set\n", listToSetPL)

listToSetPL.remove("c")
print("updated set\n", listToSetPL)

# checking wether or not the elements in the set are present or not
present = "c++" in listToSetPL
print(present, "the items exists")

# let us work on sets Logic operation
programming = {".NET", "PHP", "css", "HTML", "c", "java"}

# let us find the intersection
intersection = listToSetPL & programming
print("intersection set :", intersection)

print(programming.difference(listToSetPL), listToSetPL.difference(programming))
# this will display unique elements of listToSetPL set

# let us find there union
print(listToSetPL.union(programming))
