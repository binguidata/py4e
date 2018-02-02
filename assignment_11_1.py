"""
11.1 Write a simple program to simulate the operation of the grep command on
Unix. Ask the user to enter a regular expression and count the number of lines
that matched the regular expression:
"""

#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#$ python grep.py
#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-

#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4218 lines that matched java$

import re

regex = input('Enter a regular expression: ')
if len(regex) < 1:
    print('Please enter a valid regular expression')
    quit()

num_line = 0
fhand = open('mbox.txt')
for line in fhand:
    line.rstrip()
    list = re.findall(regex, line)
    if len(list) < 1:
        continue
    num_line = num_line + 1

print('mbox.txt had', num_line, 'lines that matched', regex)
