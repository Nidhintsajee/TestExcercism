import re
words=raw_input("Enter the word : ")
def abbreviate(words):
    regex = '[A-Z]+[a-z]*|[a-z]+'
    print ''.join(word[0].upper() for word in re.findall(regex, words))

abbreviate(words)
