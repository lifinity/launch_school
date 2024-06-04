from pprint import pp

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# cleaner to separate ternary out as a function?
# i.e. [ odd_even(num) for num in my_list ]

new_list = ['odd' if num % 2 else 'even' for num in my_list]
pp(new_list)