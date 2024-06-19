# isn't it odd?
# write a function that takes one integer arg and returns True 
# when the number's absolute value is odd, False otherwise.

def is_odd(int_):
    return bool(abs(int_) % 2)

print(f'is_odd(-3): {is_odd(-3)}')
print(f'is_odd(2): {is_odd(2)}')
print(f'is_odd(7): {is_odd(7)}')