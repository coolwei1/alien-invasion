from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

#Person
#kaiwen = {'age': 18, 'sex': 'male', #'college': 'segi'}
#print(kaiwen['age'])
#print(kaiwen['sex'].title())
#print(kaiwen['college'].upper())
#
##favorite number
#popular_number = {'kaiwen': 18, 'weihan': #4, 'chekwei': 7,'wtf': 9}
#print("Kai Wen's favorite number is " + #str(popular_number['kaiwen']))
#
##Glossary
#glossary = {
#    'print': 'use to print string, number,# etc on screen',
#    'scrip': 'use to remove space infront #and behind a string',
#    '\n': 'use to insert a blank line',
#    '\t': 'use to insert a tab',
#    'str': 'use to show a number/value in #the form of string',
#    '#': 'use to commend code',
#    '[]': 'indicate list'
#}
#
#print("Print is " + glossary['print'])