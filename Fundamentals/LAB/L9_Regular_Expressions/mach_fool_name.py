import re

data = input()
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
matches = re.findall(pattern, data)
print(' '.join(matches))