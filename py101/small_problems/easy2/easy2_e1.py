# welcome stranger
# create function that takes 2 args: list & dictionary. list will contain 2 or more
# elements that, when joined w/ spaces, will produce a person's name. dict contains
# 2 keys: title & occupation. return greeting that uses person's full name & title

def greetings(name_list, details_dict):
    full_name = ' '.join(name_list)
    title_occupation = f"{details_dict['title']} {details_dict['occupation']}"
    return f'Hello, {full_name}! Nice to have a {title_occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.