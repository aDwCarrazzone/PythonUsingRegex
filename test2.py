import re
i = 1
max = 10000
File1 = open('text.txt', 'r')
regex = re.compile(r'\b(?:{})#[^#]+#'.format (i))
string = File1.read()
itemdesc = regex.findall(string)
while i < max:
	if i < max:
		print (i)
		for word in itemdesc:
			print (word)
			i += 1
	else:
		i += 1