# q9; given the following functions & invocation, what is the output?
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

bar(foo())

# foo() called w/ no args so its param defaults to "no" but that's meaningless
# since it's never used and foo() always returns "yes", which is passed to
# bar() as its arg. param == "no" is False so the first part of bar()'s return
# statement shortcircuits to false, and foo() is never run, which leaves
# False or "no", therefore "no" is evaluated last and is the value that's returned

# !! this one messed me up; thought the first part would short-circuit entire 
# expression to False but it collapses just the and section before eval-ing or.
# versus: 'x or y and z' shortcircuiting entirely to x if x is truthy; basically
# pretend parentheses around and b/c higher precedence but still eval left-to-right
# while keeping in mind short-circuit which might skip over invalid sub-expr?