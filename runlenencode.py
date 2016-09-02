from itertools import groupby
from re import sub

string=str(raw_input("Enter the word to encode : "))
def decode(string):
    print sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


def encode(string):
    def single_helper(k, g):
        l = len(list(g))
        return k if l == 1 else str(l) + k
    print ''.join(single_helper(key, group) for key, group in groupby(string))
    
encode(string)
print 'decode the encoded string :'
decode(string)