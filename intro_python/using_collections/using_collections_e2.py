init_str = 'Launch School'
start_idx = init_str.find('c')  # can also use index() but worse opt b/c error if not found
print(init_str[start_idx:start_idx+6])