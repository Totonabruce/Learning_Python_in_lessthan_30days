import re
txt = 'I love python programming'
match = re.match('I love', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt [start:end]
print(substring)

import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None