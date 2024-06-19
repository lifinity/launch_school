# q2; write code to determine if given str ends in exclamation mark?
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def str_ends_in(str_, substr):
    return bool(str_[-1] == substr)

print(f"'{str1}' ends in '!'? {str_ends_in(str1, '!')}")
print(f"'{str2}' ends in '!'? {str_ends_in(str2, '!')}")

# actual solution was to use str1.endswith('!')