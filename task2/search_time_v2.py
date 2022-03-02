import re
s = input()
if re.search(r'\b([вВ]рем\w+)\b', s) is not None:
    print("\n".join(str(x) for x in re.findall(r'\b([вВ]рем\w+)\b', s)))
