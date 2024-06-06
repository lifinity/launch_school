# q2; fix given function to not fail for negative numbers
# bonus q; what's the purpose of number % divisor == 0 in this code?

def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

def factors2(number):
    divisor = number
    result = []
    while divisor > 0: # changed this expression
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# returns factors for negative numbers too
def factors3(number):
    divisor = abs(number)
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors3(-50))

# the purpose of number % divisor is to check if a factor exists paired against the current
# divisor; since modulus returns remainder, no remainder means number cleanly divisible thus
# the result of number // divisor returns the factor where factor * divisor = number

# solution says determines whether result of division is an integer, which is also true since
# that's another way of saying 'cleanly divisible'