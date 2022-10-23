# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
result = ""
if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "slightly overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"
string_words = "are"
if result == "normal weight":
    string_words = "have a"
print(f'Your BMI is {int(bmi + 0.5)}, you {string_words} {result}.')
