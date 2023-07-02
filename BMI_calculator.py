import math
#age = int(input('Enter your age in integers, posistive values:'))
height = int(input('Enter your height in inches, posistive values:'))
weight = int(input('Enter your weight in and lbs, posistive values only:'))
#if ( age < 0 or weight < 0 or height < 0):
if ( weight < 0 or height < 0):
    print('Enter "only" Postive values for height and weight')
    exit(1)

calc_bmi = float(weight*703/(height ** 2))

if calc_bmi < 16.0:
# S under weight
    weight_cat = 'Severly underweight'
#under weight
elif calc_bmi >= 16.0 and calc_bmi < 18.9:
    weight_cat = 'Underweight'
# Normal
elif calc_bmi >= 18.5 and calc_bmi < 24.9:
    weight_cat = 'Normal'
# Overwight
elif calc_bmi >= 25.0 and calc_bmi < 29.9:
    weight_cat = 'overweight'
# Moderately Obese
elif calc_bmi >= 30 and calc_bmi < 34.9:
    weight_cat = 'Moderately Obese'
# Severly Obese
elif calc_bmi >= 35 and calc_bmi < 39.9:
    weight_cat = 'Severly Obese'
# Morbidly Obese
else:
    weight_cat = 'Morbidly Obese'
calc_bmir = round(calc_bmi,1)
## truncation can be done via
# round and {float:.numberf} number should be >= 2
#print(f'Your BMI is {calc_bmi:.2f} places you on {weight_cat}' )
print(f'Your BMI is {calc_bmir} places you on {weight_cat}' )