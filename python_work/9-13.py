from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = 'use to print string, number,# etc on screen'

glossary['scrip'] = 'use to remove space infront #and behind a string'

glossary['str'] = 'use to show a number/value in #the form of string'
#Glossary

for fn, pur in glossary.items():
	print(fn.title() + " is " + pur)