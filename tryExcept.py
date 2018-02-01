astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr2 = '123'
try:
    istr2 = int(astr2)
except:
    istr2 = -1
print('Second', istr2)

rawstr = input('Enter a number:\n')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
