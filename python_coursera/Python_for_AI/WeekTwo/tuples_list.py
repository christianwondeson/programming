# list are changable ordered sequence that can be accessed by indexing format
L = ["Michael Jackson", 10.1, 1982]
print(L)

print(
    "the same element using negative and positive indexing:\n Postive:",
    L[0],
    "\n Negative:",
    L[-3],
)
print(
    "the same element using negative and positive indexing:\n Postive:",
    L[1],
    "\n Negative:",
    L[-2],
)
print(
    "the same element using negative and positive indexing:\n Postive:",
    L[2],
    "\n Negative:",
    L[-1],
)

# list can nest tuples
information = ["chris_bow", 24, ("CE, 3.78"), ["AA", 20190]]
print(information)

# list and tuple operations are more or less the same
print(information[1:4])
print(information[::1])

# adding elements in to our list of elements
information.extend(["gym enthusiast", 70])
print(information, len(information))

# the other method is appending to the list of elements
information.append(["help me nigga", 12.5])
print(information, len(information))
# list can be changed
information[0] = "christian"
print(information)

del information[1]
# this function will delete our list 2nd element
print(information)

print(information[-1][0].split())

# if we want to clone our list 
userOne = information[:]
print(userOne)
# userOne will know refer different address list with the same content of information

# next up tuples
# what makes tuple different from list it is unchangeable ordered sequence that can be accessed by using Zero indexing method
tuplePl = ("liva", "Arse", "city")
print(tuplePl)
type(tuplePl)
# this type is tuple
# all the method we applied to the list also applies to tuples except from changing each element.
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)
