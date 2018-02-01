"""
3.2 Rewrite your pay program using try and except so that your program
handles non-numeric input gracefully by printing a message and exiting the
program. The following shows two executions of the program:
"""

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = 0
r = 0
try:
    h = float(hours)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = 0
if h > 40:
    pay = 1.5*h*r - 20*r
else:
    pay = h * r
print(pay)
