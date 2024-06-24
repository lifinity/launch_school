# grade book
# write function that determines avg of 3 scores passed in & returns associated
# letter grade; assume no negatives or scores > 100

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D
# 0 <= score < 60: 'F'

def get_grade(*scores):
    grade_map = {
        (90, 101): 'A',
        (80, 90): 'B',
        (70, 80): 'C',
        (60, 70): 'D',
        (0, 60): 'F',
    }

    mean = sum(scores) / len(scores)
    for (score_floor, score_ceil), letter_grade in grade_map.items():
        # turns out float in range(x, y) returns False
        if score_floor <= mean < score_ceil: 
            return letter_grade
    return "Grade can't be computed. Check if invalid scores included."

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
print(get_grade(100, 100, 100) == "A")   # True
print(get_grade(80, 80, 80) == "B")      # True
print(get_grade(80, 80, 80) == "C")      # False

