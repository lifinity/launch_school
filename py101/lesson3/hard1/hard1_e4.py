# q4; given an incomplete function that's meant to determine whether an input string  
# is an ip address using 4 dot-separated numbers, e.g. 10.4.5.11; fix it so that it
# 1) returns a false condition when the input isn't an ip
# 2) handles the case when the input str has more/less than 4 components 
# e.g. 4.5.5 or 1.2.3.4.5 should both be invalid
def is_an_ip_number(str_):
    if str_.isdigit():
        number = int(str_)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

def is_dot_separated_ip_address2(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4: # fulfills 1 & 2
        return False 
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False # changed to fulfill 1

    return True