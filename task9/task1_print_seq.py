from itertools import permutations
print("\n".join(str(x).replace(')', '').replace('(', '').replace(',', '').replace(' ', '')
                for x in (list(permutations([i for i in range(1, int(input()) + 1)])))))
