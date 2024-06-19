def uppercase_long_strs(str_):
    return (str_.upper() if len(str_) > 10 else str_)

print(uppercase_long_strs('hello world'))
print(uppercase_long_strs('goodbye'))