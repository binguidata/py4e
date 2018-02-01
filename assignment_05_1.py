"""
5.1 Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try
and except and print an error message and skip to the next number.
"""

#output:
#Invalid input
#Maximum is 7
#Minimum is 4

count = 0
total = 0.0
while True:
    num = input("Enter a number: ")
    if num == "done" : break # break escape the loop (while)
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue # back to the beginning of the loop (while)
    count = count + 1
    total = total + fnum

print("total is", total)
print("count is", count)
print("average is", total/count)
