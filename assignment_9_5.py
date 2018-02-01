"""
9.5 This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e., the whole email
address). At the end of the program, print out the contents of your dictionary.
"""

#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    quit()

domains = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    pieces = words[1].split('@')
    domains[pieces[1]] = domains.get(pieces[1], 0) + 1

print(domains)
