# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')
print(f'original stuff: {stuff}')

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(f'new stuff: {stuff}')