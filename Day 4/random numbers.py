# random numbers

import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()

print((random_float * 10))

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

head_or_tale = random.randint(1,2)
if head_or_tale == 1:
    print("Head")
if head_or_tale == 2:
    print("Tale")