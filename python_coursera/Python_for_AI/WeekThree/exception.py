# def safe_divide(numerator, denominator):
#     try:
#         result = numerator / denominator
#         return result
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
#         return None

# numOne = int(input("Please enter the numerator value :- "))
# numTwo = int(input("Please enter the denominator value :- "))
# safe_divide(numOne, numTwo)
str = "()"
def isParenthesesvalid(str):
    stack = []
    print(type(stack))
    mapping = {
        
        "(" : ")",
        "[" : "]",
        "{" : "}",
    }
    for char in str:
        if char in mapping:
            stack.append(char)
            print(stack)
        elif stack and char == mapping[stack[-1]]:
            stack.pop()
            print(stack)
        else:
            return False
    return not stack

print(isParenthesesvalid(str))