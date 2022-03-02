# Created by Samohin Artem
# Date 2019-12-21
# Task Description: http://www.hostedredmine.com/issues/803197

import re

s = input()
print("\n".join(str(x[0])[0:len(x[0]) - 1] for x in re.findall(r'(\w+([.]|[!]|[?]))', s)))
