"""
10.3 Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies.
"""

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabets = list(alphabet)
pool_list = list()
pool_dict = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter not in alphabets:
                continue
            pool_list.append(letter)
            pool_dict[letter] = pool_dict.get(letter, 0) + 1
#print(pool_dict)

pool_dict_sorted = sorted([(v,k) for k,v in pool_dict.items()], reverse = True)
#print(pool_dict_sorted)

for k, v in pool_dict_sorted.items():
    print(v, k)
