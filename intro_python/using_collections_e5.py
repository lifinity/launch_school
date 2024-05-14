'cat'                             # ok to use
(3, 1, 4, 1, 5, 9, 2)             # ok. immutable (including all elements so hashable)
['a', 'b']                        # no. mutable, not hashable
{'a': 1, 'b': 2}                  # no. mutable, not hashable
range(5)                          # ok. immutable
{1, 4, 9, 16, 25}                 # no. mutable, not hashable
3                                 # ok to use
0.0                               # ok to use
frozenset({1, 4, 9, 16, 25})      # ok. immutable
