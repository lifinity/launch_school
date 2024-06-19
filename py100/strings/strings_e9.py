# check prefix
def starts_with(str_, prefix):
    return str_.startswith(prefix)
    # return str_[0:len(prefix)] == prefix

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True