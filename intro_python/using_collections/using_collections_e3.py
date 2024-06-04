init_tuple = (1, 2, 3, 4, 5)
new_tuple = list(init_tuple[1:-1])
new_tuple.reverse()
new_tuple = tuple(new_tuple)

new_tuple2 = init_tuple[-2:0:-1]
print(new_tuple2)