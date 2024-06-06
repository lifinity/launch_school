# q3; given 2 implementations of a rolling buffer (can add or remove elements but once 
# buffer full, new elements displace oldest), what're the differences, if any?
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# 2nd implementation initializes local variable buffer with a new list created from
# concatenating value of buffer arg passed in w/ a list containing new_element
# 1st references same buffer obj that's passed in as arg & mutates it; this mutates
# the original buffer from an outer scope as well