def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# prints 'Hello World' b/c when outer() is invoked
# on line 10 and runs, its body contains a function call 
# to nested function inner() on line 8 which prints
# outer_var, accessed via lexical scope from encapsulating
# scope of outer(), then inner()'s local variable inner_var