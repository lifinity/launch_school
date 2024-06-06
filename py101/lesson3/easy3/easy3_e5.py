# q5; rewrite given function so only 1 return that doesn't explicitly use True or False
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_color_valid2(color):
    # return color == "blue" or color == "green"
    return color in ["blue", "green"]