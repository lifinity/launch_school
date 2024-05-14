obj = 42              # INIT
obj = 'ABcd'          # reassign
obj.upper()           # neither; separate string produced but not assigned into obj
obj = obj.lower()     # reassign; strings immutable
print(len(obj))       # neither; prints property of obj w/o changing it
obj = list(obj)       # reassign; strings immutable
obj.pop()             # mutation; got rid of last list element
obj[2] = 'X'          # mutation; reassigned one list element
obj.sort()            # mutation; reordered list elements (in-place)
set(obj)              # neither, new/separate set initialized
obj = tuple(obj)      # reassign