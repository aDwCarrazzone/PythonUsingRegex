import re
File1 = open('test', 'r')
regex = re.compile(r'\b(?:22822)#[^#]+#')
string = File1.read()
itemdesc = regex.findall(string)
	for word in itemdesc: print (word)