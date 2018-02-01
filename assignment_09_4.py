"""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the most commits. The program looks for 'From ' lines and takes the second
word of those lines as the person who sent the mail. The program creates a
Python dictionary that maps the senders mail address to a count of the number
of times they appear in the file. After the dictionary is produced, the
program reads through the dictionary using a maximum loop to find the most
prolific committer.
"""

#output
#cwen@iupui.edu 5

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

emails = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    emails[words[1]] = emails.get(words[1], 0) + 1

imax = None
sender = ''
for email, num in emails.items():
    if imax is None or imax < num:
        imax = num
        sender = email

print(sender, imax)
