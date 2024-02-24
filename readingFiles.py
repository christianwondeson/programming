# with open('./python_coursera/words.txt', 'r') as f:
#     for line in f.readlines():
#         line.find("O")
#         print(line.rstrip().upper())

input = "()"


def isValid(input):
    stack = []
    mapping = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for index, char in enumerate(input):
        if char in mapping:
            stack.append(char)
            print(stack)
            print(index, char)
        elif stack and char == mapping[stack[-1]]:
            print(index, char == mapping[stack[-1]])
            stack.pop()
            print(stack)
        else:
            return False
    return not stack


isValid(input)

# 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
