# q5; what do you think following code will output?
# bonus q; how can you reliably test if a value is nan/NaN
nan_value = float("nan")

print(nan_value == float("nan"))

# i want this to be True but it's probably False b/c NaN not equal to NaN or smth
# isnan() method as part of python's math module is one way to reliably test if nan/NaN

# update: yeah it was False. 
# solution says python doesn't let you use == to determine if number is nan.