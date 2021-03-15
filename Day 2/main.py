# Data Types

# String

'''
print("Hello"[4])

print("123" + "345")  # Concatenation

# Integer

print(123 + 345)

print(123_456_789)

# Float
print(3141.5)

# Boolean
print(True)
print(False)

num_char = len(input("What is your name?"))

print(type(num_char))

# Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

a = float(123)
print(type(a))
'''

3 + 5
7 - 4
3 * 2
print(2 ** 2)  # power
print(type(6 / 3))

'''
PEMDAS

()
**
* /
+ -

'''
print(3*3+3/3-3)
print(3*(3+3)/3-3)

print(type(4//2))
#Round

print(round(8/3, 2))

score = 0
height = 1.8
isWinning = True
#f-string
print(f"your score is {score},your height is {height},you are winning is {isWinning}")