"""
5.2 Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead
of the average.
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
