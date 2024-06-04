# are we moving?
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# is_moving evaluates to True so that's whats printed out
# parentheses required b/c and has higher operator precedence than or
# w/o them: (braking_force < acceleration and speed > 0) or acceleration > 0