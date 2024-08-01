# w/o running, what does the following code return?
lst = [1, 2, 3, 4, 5]
lst[:2]

# doesn't 'return' anything & nothing printed to console
# lst[:2]'s value not captured in any variable but it evals
# to [1, 2] b/c slice of lst starting from index 0 (default)
# to index 2 exclusive, so really only elements @ idx 0 & 1
# included in the slice.