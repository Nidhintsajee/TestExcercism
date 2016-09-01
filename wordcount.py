import re
txt=raw_input("Enter the phrase : ")
def word_count(txt):
	phrase=list(txt.split(" "))
	dict={}
	for sentence in phrase:
		for word in re.split('\s',sentence):
			try:
				dict[word] += 1
			except KeyError:
				dict[word] = 1

	print "Word Count --> " , dict
		
word_count(txt)
