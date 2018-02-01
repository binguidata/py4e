"""
10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the
hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below. Note that the autograder does not have support
for the sorted() function.
"""

#output:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

hours = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue
    pieces = words[5].split(':')
    hours[pieces[0]] = hours.get(pieces[0], 0) + 1

#tmp = sorted(hours.items())

# do not use sorted() function
tmp = list()
for k, v in hours.items():
    tmp.append((k, v))
tmp_sort = list()
while tmp:
    min_k = None
    min_v = None
    for k, v in tmp:
        if (min_k is None and min_v is None) or k < min_k:
            min_k = k
            min_v = v
    tmp_sort.append((min_k, min_v))
    tmp.remove((min_k, min_v))

for k, v in tmp_sort:
    print(k, v)
