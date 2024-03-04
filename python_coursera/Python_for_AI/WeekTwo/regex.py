# this code will explain about some method of regex expression
import re

sOne = "Michael Jackson is the best"

pattern = "Jackson"

result = re.search(pattern, sOne)
if result:
    print("match found!")
else:
    print("match not found!")


pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# this code will explain using \d\d\d\d\d\d\d\d will select my 0-9 digits

pattern = "\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("matches:", matches)

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)

# Write your code below and press Shift+Enter to execute

d = "ABCDEFG"

print(d[0:3])


# Write your code below and press Shift+Enter to execute
f2 = "YOU ARE RIGHT"
print(f2.lower())

# Write your code below and press Shift+Enter to execute

f = "You are wrong"
print(f.upper())


g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(g.find("snow"))

# Write your code below and press Shift+Enter to execute
print(g.replace("Mary", "Bob"))

g.replace(",", ".")

str2 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

# Write your code below and press Shift+Enter to execute
new_str2 = re.findall(r"woo", str2)
print(new_str2)


str1 = "The quick brown fox jumps over the lazy dog."

# Write your code below and press Shift+Enter to execute
new_str1 = re.sub(r"fox", "bear", str1)
print(new_str1)

s3 = "House number- 1105"
# Write your code below and press Shift+Enter to execute
result = re.search("\d", s3)

# Check if a match was found
if result:
    print("Digit found")
else:
    print("Digit not found.")
