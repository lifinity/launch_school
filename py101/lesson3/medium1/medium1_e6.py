# q6; what's output of following code?
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# prints 34 b/c python's pass-by-obj-reference but it's contigent on original
# reference's mutability, and primitives like int (what answer is) are immutable
# therefore mess_with_it() doesn't actually change the reference passed to it and 
# simply returns a separate value. ergo, answer is still 42, 42 - 8 is 34