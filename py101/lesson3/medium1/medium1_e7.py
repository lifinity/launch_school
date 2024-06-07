# q7; are any messes (mutations) caused by running the following function on given data?
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# yes b/c dictionarys are a mutable collection & mess_with_demographics() is accessing
# the original dictionary via reference passed in and mutating the nested dictionaries
# for each family member directly