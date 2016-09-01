que=raw_input("Hai, its me Bob anything to ask ? ")
def bob(que):	
	if que == "_":
		print "Fine. Be that way !"	
	elif que.endswith("!"):
		print "WHOA , chill out !"	
	elif que.endswith('?'):
		print "Sure."
	else:
		print "Whatever."

bob(que)