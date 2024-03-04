import re
sum = 0
with open('./python_coursera/words.txt', 'r') as f:
    for line in f:
        total = re.findall('\b[wW]\w+', line.rstrip())
        for num in total:
            sum += int(num)
print(sum)
# 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
