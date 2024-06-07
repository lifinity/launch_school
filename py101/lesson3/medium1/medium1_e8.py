# q8; given the following function, what is the output of this invocation chain?
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# most nested one, rps("rock", "paper"), rps("rock", "scissors") returns 
# "paper" and "rock" respectively, which means the invocation encapsulating
# it becomes rps("paper", "rock"), which returns "paper". the outermost
# function call becomes rps("paper", "rock") which ultimately prints "paper" 