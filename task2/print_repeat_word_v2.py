import re
s = input()
print("\n".join(str(x) for x in re.findall(r'\b(\w+)\b\s+\b\1\b', s)))
