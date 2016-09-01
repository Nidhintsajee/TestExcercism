from functools import reduce
s=raw_input("Enter the Hexadecimal number : ")

def hexa(s):
    s = s.lower()
    if set(s) - set('0123456789abcdef'):
        raise ValueError('Invalid hexadecimal string')
    l = [ord(c) - ord('a') + 10 if c in 'abcdef' else ord(c) - ord('0')
         for c in s]
    print reduce(lambda x, y: x * 16 + y, l, 0)

hexa(s)
