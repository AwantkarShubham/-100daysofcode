students_height = [180, 124, 165, 173, 189, 169, 146]
total = 0
lenght = 0
for i in students_height:
    total += i
    lenght += 1

avg = (total / lenght)
print(total)
print(round(avg))
