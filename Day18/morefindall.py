import re
txt = 'Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'
matches = re.findall ('python',txt, re.I)
print(matches)


