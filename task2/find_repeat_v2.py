import re
s = input()
#print(re.sub(r'\b(\w+)\b(.+)\b(\1)\b', r'\1\2', s))
print(re.sub(r'\b(\w+)\b\s\b(\1)\b', r'\1', s))
