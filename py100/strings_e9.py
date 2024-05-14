# check prefix
def starts_with(str, prefix):
    return str.startswith(prefix)
    # return str[0:len(prefix)] == prefix

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True