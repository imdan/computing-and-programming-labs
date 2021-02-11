weight_lbs = float(input("Please enter weight in pounds: "))
height_inches = float(input("Please enter height in inches: "))

weight_kg = weight_lbs * 0.453592
height_m = height_inches * 0.0254

bmi = weight_kg / height_m**2

print("BMI is:", bmi)
