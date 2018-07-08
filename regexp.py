#OK THIS IS NEW
'''
import re
pattern="this"
text="Does  this text this match the pattern?"
match=re.search(pattern,text)
print (match.start(),match.end())

import re
regexes=[re.compile(p) for p in ["this","that"]]
print (regexes)
text='Does this text match the pattern'
for regex in regexes:
	print (regex)
	print ('Seekinh "{}"=>'.format(regex.pattern))
	if(regex.search(text)):
		print ("Match")
	else:
		print ("No Match")

import re
text="abbaaabbbbaaaaa"
pattern='ab'
a=re.findall(pattern,text)
print (len(a))

import re
text="abbaaabbbbaaaaa"
pattern="ab"
b=re.finditer(pattern,text)
for x in b:
	print (x.start(),x.end())
'''
