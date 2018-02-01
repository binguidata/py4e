"""
10.1 Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line. Count the number of messages from each
person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in reverse order and print out the person who has the most commits.
"""

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

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

"""
counter = list()
for k, v in emails.items():
    counter.append((v, k))
counter = sorted(counter, reverse=True)
"""

counter = sorted([(v, k) for k, v in emails.items()], reverse=True)

print(counter[0][1], counter[0][0])
