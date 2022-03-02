# Created by Samohin Artem
# Date 2018-10-24
# Task Description: http://www.hostedredmine.com/issues/779695


def CountSort(A):
    t = [0]*101
    for i in A:
        t[i] += 1
    A =[]
    for i in range(101):
        A += [i]*t[i]
    return A

B = [int(22),int(3),int(3),int(13),int(3),int(3),int(3),int(3),int(31),int(3)]

print(CountSort(B))