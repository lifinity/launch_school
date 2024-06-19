# floating point arithmetic
# write program that prompts user for 2 positive numbers (floats) & prints results
# of operations on these 2 numbers: addition, subtraction, product, quotient, 
# floor quotient, remainder & power; don't worry about validating input

def prefix_print(str_, prefix="==> "):
    print(f"{prefix}{str_}")

# as per official solution
def calculate(a, b, op):
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b
        case '//': return a // b
        case '%': return a % b
        case '**': return a ** b

def float_ops():
    prefix_print("Enter the first number: ")
    float1 = float(input())

    prefix_print("Enter the second number: ")
    float2 = float(input())

    for op in ['+', '-', '*', '/', '//', '%', '**']:
        prefix_print(f"{float1} {op} {float2} = {calculate(float1, float2, op)}")

    '''
    prefix_print(f"{float1} + {float2} = {float1 + float2}")
    prefix_print(f"{float1} - {float2} = {float1 - float2}")
    prefix_print(f"{float1} * {float2} = {float1 * float2}")
    prefix_print(f"{float1} / {float2} = {float1 / float2}")
    prefix_print(f"{float1} // {float2} = {float1 // float2}")
    prefix_print(f"{float1} % {float2} = {float1 % float2}")
    prefix_print(f"{float1} ** {float2} = {float1 ** float2}")
    '''

float_ops()
