import re
data = input()
patthern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'

matches = re.finditer(patthern, data)

matches = [m.group(0) for m in matches]
print(*matches,sep=', ')