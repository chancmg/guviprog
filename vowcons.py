x=raw_input('enter the character')
if(len(x)>1):
	print 'Enter single character!!'
else:
	if('a' in x or 'e' in x or'i' in x or'o' in x or'u' in x):
		print 'vowel'
	else:
		print 'consonant'