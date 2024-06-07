# q1; will the following functions return the same results
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# second() looks like it'll return None b/c the opening brace for the dict
# isn't on the same line as return so it doesn't register it as part of the
# return statement and instead treats it as inaccessible code that never runs

# update; yyyep. first() returns the dict like normal, second() returns None