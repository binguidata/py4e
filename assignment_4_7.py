"""
4.7 Rewrite the grade program from the previous chapter using a function
called computegrade() that takes a score as its parameter and returns a grade as
a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and
exit.
"""

def computegrade(score):
    if 0.9 <= score <= 1:
        return "A"
    elif 0.8 <= score < 0.9:
        return "B"
    elif 0.7 <= score < 0.8:
        return "C"
    elif 0.6 <= score < 0.7:
        return "D"
    elif 0.0 <= score < 0.6:
        return "F"
    else:
        return "Error."

s = input("Enter your score:")
fs = 0.0
try:
    fs = float(s)
except:
    Print("Error: please enter numeric input")
    fs = -1.0
    quit()

if 0.0 <= fs <= 1:
    ys = computegrade(fs)
    print("Your grade is", ys)
else:
    print("No grade matches to the input score")
    quit()
