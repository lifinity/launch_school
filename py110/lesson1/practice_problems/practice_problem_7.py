# w/o running it, what would following code output?
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# prints ['bear'] i.e. list of strs w/ len > 3 from list words