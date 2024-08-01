# given following tuple, how to count num occurrences "banana"
fruits = ("apple", "banana", "cherry", "date", "banana")

# answer
print(fruits.count("banana"))

# alt; bonus: get a list of all indices w/ val "banana" to do smth w/
banana_occurrences = [idx for idx, val in enumerate(fruits) if val == "banana"]
print(banana_occurrences)
print(len(banana_occurrences))

# alt; can also use regular loop & counter
count = 0
for fruit in fruits:
    count += 1 if fruit == "banana" else 0
print(count)