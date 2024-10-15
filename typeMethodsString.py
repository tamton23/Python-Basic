s = 'Spam'
# Find the offset of a substring
print(s.find('pa'))
# Replace occurrences of a substring with another
print(s.replace('pa','XYZ'))
# Split on a delimiter into a list of substrings
line = 'aa,bb,ccc,d'
print(line.split(','))
#Upper- and lowercase conversions
print(line.upper())
print(line.lower())
# Content tests: isalpha, isdigit, etc.
a = 'abc'
b = '4'
print(a.isalpha())
print(b.isdigit())
# Remove whitespace characters on the right side
line = 'aaa,bbb,cc\n'
print(line.rstrip())

# Formatting expression (all)
news = '%s, eggs, and %s' %('spam', 'SPAM!')
print(news)

# Formatting method (2.6, 3.0)
news1 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
print(news1)
