"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a
line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in
the line (i.e. the entire address of the person who sent the message). Then
print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at
http://www.pythonlearn.com/code/mbox-short.txt
"""

#output:
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#....
#cwen@iupui.edu
#There were 27 lines in the file with From as the first word

fname = input('Enter the file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
words = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement (order is important)
    if len(words) < 2 or words[0] != 'From':
        continue
    print(words[1])
    count = count + 1
print('There were %d lines in the file with From as the first word' %count)
