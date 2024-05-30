def my_func():
    num = 10

my_func()
print(num)

# throws a NameError, complains about variable 
# being undefined b/c num purely local to my_func()
# so can't access it in/from outer scopes 