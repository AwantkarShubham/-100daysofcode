score = [10, 20, 30, 40, 80, 60, 50, 70, 100]
score = sorted(score)
print(score)
for i in range(len(score)):
    for j in range(len(score)):
        if score[i] > score[j]:
            highest = score[i]
            break
print(highest)
