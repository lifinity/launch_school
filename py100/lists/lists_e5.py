# filter
scores = [96, 47, 113, 89, 100, 102]

above100 = 0
for score in scores:
    above100 += (1 if score >= 100 else 0)

print(above100)

# print(len([score for score in scores if score >= 100]))