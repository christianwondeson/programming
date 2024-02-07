# frint("Hello, world!")
# this code will raise a Name error because python doesn't recognize frint as a python builtin function

# print("Hello,world!)
# this also raises an error where the string is not closed properly this kind of typo errors is called syntax errors

# since python is oopl everything is an object starting from simple data types example :- integer, float, string
print(type("help me nigger"), type(12.4), type(3))
# the process of changing the data type in python or any other programming is called typecasting
# lets try to chang an integer to a float
print(type(float(3)))
print(type(int('22')))

# the next statement will raise a value error
# print(int('this is'))

print(type(int(True)), type(int(False)), type(bool(0)), type(bool(1)))

# next up we will see variables and arithmetic expressions 
# for instance // sign is used for integer division 
print((120 * 3) + 32 -12)
def payroll(hours, rate):
    payments = hours * rate
    if hours == 0:
        print("please work harder to get payed")
        # this code wil raise an error because we never define a variable called payment to use it 
    return payments
    
print(payroll(12, 20))
print(payroll(0, 20))
# the above expression will first execute the parenthesis, then the plus sign, then the minus sign

# working with strings
name = "Michael Jackson"
print(name)
print(name[-1], len(name), name[0:4], name[::2])
#  this are different methods of slice strings in python. since we know that string are a sequence of characters in order to access this character we use index like 0 based indexs

print(r" my email address \ phone number")
print('phone number \ email address\ posatal code \ website address')
# the above statment will use the escape sequences for our string representation

# string manipluations
name_one = name.upper()
print(name_one)
name_one = name.lower()
print(name_one)
name_three = name.replace('Michael', 'Janet')
print(name_three)
print(name.find('j'))
print(name.find('bb'))
# this must return -1 since the substring bb is not found on the name variable
# using split method to separate string variables in to array of strings