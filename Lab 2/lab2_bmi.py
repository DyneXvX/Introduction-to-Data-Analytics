# %%
def bmi():
    print('Welcome to the body mass index (BMI) calculator.')
    weight = int(input('Enter your weight in pounds: '))
    height = int(input('Enter your height in inches: '))
    bmi = (weight * 703) / (height * height)

    if bmi < 18.5:
        message = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        message = "normal"
    elif bmi >= 25 and bmi <= 29.9:
        message = "overweight"
    else:
        message = "obese"

    print('Your BMI is {bmi: .2f}. According to NIH, you are {message}'.format(
        **locals()))
    print()


# %%

# BMI = (weight in pounds x 703) / (height in inches x height in inches)
# BMI Values

# Underweight: less than 18.5

# Normal: between 18.5 and 24.9

# Overweight: between 25 and 29.9

# Obese: 30 or greater
