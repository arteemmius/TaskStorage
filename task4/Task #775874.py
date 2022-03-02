def sum(a, b):
    if int(b)!= 0:
        b -= 1
        a += 1
        return sum(a, b)

    return a

print(sum(17, 12))