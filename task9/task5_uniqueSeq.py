from itertools import takewhile
print(len(set([int(item) for item in
               list(takewhile(lambda x: x != "", input().split(' ')))])))
