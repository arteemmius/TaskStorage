from functools import reduce
from itertools import takewhile

print(reduce(lambda x, y: x * y, [int(item)**5 for item in
                                  list(takewhile(lambda x: x != "", input().split(' ')))]))
