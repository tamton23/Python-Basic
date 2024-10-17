import re
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/tam')
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.groups())
match2 = re.match('Hello [ \t]*(.*)world', 'Hello 	Python world')
print(match2.group(1))
