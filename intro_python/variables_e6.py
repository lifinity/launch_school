# also didn't name this age.py; no error-check for invalid non-numerical inputs
current_age = int(input('Enter your current age: '))
for future_yrs in range(10, 50, 10):
    print(f'In {future_yrs} years, you will be {current_age + future_yrs} years old.')