# q1; output 'The Flintstones Rock!' 10x w/ each line prefixed by one more '-'

def print_flintstones(num_times):
    for i in range(0,num_times):
        print(f"{'-' * i}The Flintstones Rock!")

print_flintstones(10)