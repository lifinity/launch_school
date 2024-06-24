# right triangles
# write a function that takes a positive int n & prints a right triangle
# whose sides have n stars; the hypotenuse (diagonal) of triangle should
# have one end @ lower-left of triangle & other at upper-right

def triangle(n):
    for row in range(1, n+1):
        print(f"{('*' * row):>{n}}")
        # print(('*' * row).rjust(n))

triangle(5)
triangle(9)