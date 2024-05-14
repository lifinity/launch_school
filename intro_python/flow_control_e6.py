def uppercase_long_strs(str):
    return (str.upper() if len(str) > 10 else str)

print(uppercase_long_strs('hello world'))
print(uppercase_long_strs('goodbye'))