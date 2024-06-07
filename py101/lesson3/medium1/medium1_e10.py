# q10; given the following code, what's the output? keep in mind interning
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# prints True b/c even tho a and b initialize to 42 separately, the id of the primitive int obj 
# they're pointing to is the same b/c of interning; and then c is set to reference the same obj
# as a which means the id of what its pointing at is definitely equal to a & transitively, b