"""
7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case. Use
the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
"""

#output:
#WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE
#AND REWARDING ACTIVITY  YOU CAN WRITE PROGRAMS FOR
#....
#AND MIND-NUMBING

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    print(line)
