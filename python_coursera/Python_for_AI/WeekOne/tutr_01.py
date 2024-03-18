num1, num2 = input("Enter two numbers: ").split()
operator = input("Enter the operation you want to operate\n")

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Error: Division by zero!"
}

num1 = int(num1)
num2 = int(num2)

result = operations.get(operator, lambda x, y: "Error: Invalid operator!")(num1, num2)
print(result)

# this is meters coveter
miles = input("please enter relevant mile to be converted: ")

def milesToKilo(inputmiles):
    return float(inputmiles * 1.60934)

print("miles to kilometer converstion")
print(f"{miles} to kilometers {milesToKilo(int(miles))}")
# print("miles {} to kilometers {}".format(int(miles), milesToKilo(int(miles))))


