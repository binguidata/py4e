"""
7.2 Write a program that prompts for a file name, then opens that file and
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and output the average of those values and produce an output as shown below.
You can download the sample data at
http://www.pythonlearn.com/code/mbox-short.txt when you are testing below
enter mbox-short.txt as the file name.
"""

#output:
#Average spam confidence: 0.750718518519

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
num_sum = 0
num_count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        #print(line)
        ipos = line.find(':')
        value = line[ipos+1: ]
        try:
            num = float(value)
        except:
            continue
        num_sum = num_sum + num
        num_count = num_count + 1
print('Average spam confidence:', num_sum/num_count)
