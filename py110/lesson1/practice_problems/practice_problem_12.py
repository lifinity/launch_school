# w/o running, what's the output of the following code?
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# AttributeError; frozenset doesn't have attribute (method) 'add' 
# b/c its an immutable collection; sets are mutable and do, though