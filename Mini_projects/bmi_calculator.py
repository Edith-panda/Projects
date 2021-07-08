print("this program is to calculate your bmi ")
name = input("enter name")
height = float(input (" enter your height in metres: " ) )
weight = float(input (" enter your weight in kg: " ) )

bmi = weight / (height ** 2)
if bmi < 18 : 
    print ( f"{name } is underweight by {bmi} BMI ") 
if bmi > 25:
        print ( f"{name} is overweight by {bmi} BMI")
if 18< bmi < 25:
        print  ( f"{name} is normal by {bmi} BMI")
