from string import ascii_lowercase
sentence=raw_input("Enter the sentence : ")

def is_pangram(sentence):
    print all(char in sentence.lower() for char in ascii_lowercase)

is_pangram(sentence)
