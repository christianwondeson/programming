# let pratice on dictionaries
# What are Dictionaries?
# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.

# The best example of a dictionary can be accessing person's detais using the social security number.
# Here the social security number which is a unique number will be the key and the details of the people will be the values associated with it.

information = {
    "name": "christian",
    "age":24,
    "city": "Addis Ababa",
    "cell phone": 251945332223,
    "BMI":(1.78, 69)
}
# this is a new dictionary
print(information["name"])