text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# print(text[21:35]) gives us 'for the fjords!'
# this is the string rfind() is working w/ bc slicing returns a new str
# since it's rfind() aka reverse find, looks for 'f' starting from tail
# finds it at -7, then accounting for start idx: len('for the fjords') = 15, 15 - 7 = 8

# print(text.rfind('f', 21, 35)) is still working w/ the original full text
# in this case rfind() still finds 'f' at -7, since it's looking at the same
# section of text btwn idx 21 - 35, i.e. 'for the fjords!', but len(text) = 36, 36 - 7 = 29