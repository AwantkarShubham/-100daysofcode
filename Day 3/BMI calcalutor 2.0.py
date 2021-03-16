height = input("Enter your height in m:")
weight = input("Enter weight in Kg:")
Bmi = float(weight) / float(height) ** 2
if Bmi < 18.5:
    print("underweight")
elif Bmi < 25:
    print("normal weight")
elif Bmi < 30:
    print("overweight")
elif Bmi < 35:
    print("obese")
else:
    print("clinically obese")
print(int(Bmi))
