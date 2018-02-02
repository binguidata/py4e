"""
11.2 Write a program to look for lines of the form
`New Revision: 39772`
and extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.
"""

#Enter file:mbox.txt
#38549.7949721

#Enter file:mbox-short.txt
#39756.9259259

import re

fname = input('Enter file:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

list_num = list()
for line in fhand:
    line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) != 1:
        continue
    list_num.append(float(x[0]))

average_num = sum(list_num) / len(list_num)
print('%.7f' %average_num)
