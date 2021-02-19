weight = float(input("Please enter weight in kilograms: "))

height = float(input("Please enter height in meters: "))

bmi = round(weight / height**2, 2)

if (0 <= bmi <= 18.4):
    status = "Underweight"
elif (18.5 <= bmi <= 24.9):
    status = "Normal"
elif (25 <= bmi <= 29.9):
    status = "Overweight"
elif (bmi > 30):
    status = "Obese"
else:
    status = "Unavailable"

print("BMI is: ", bmi, ", Status is ", status, sep="")
