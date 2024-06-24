# repeat yourself
# write a function that takes 2 args, a str and a positive int
# & prints the str as many times as the int indicates

def repeat(str_, int_):
    for _ in range(int_):
        print(str_)

repeat('Hello', 3)