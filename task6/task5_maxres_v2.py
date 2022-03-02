# Created by Samohin Artem
# Date 2018-10-24
# Task Description: http://www.hostedredmine.com/issues/779674

dataSchool = list()
for line in open('input.txt', 'r', encoding='utf8'):
    line = line.replace('\n', '').split(' ')
    line.pop(1)
    line.pop(0)
    if not dataSchool or \
            not(line[0] in [dataSchool[i][0] for i in range(0, len(dataSchool))]):
        dataSchool.append(line)
    if line[0] in [dataSchool[i][0] for i in range(0, len(dataSchool))]:
        for j in range(0, len(dataSchool)):
            if int(dataSchool[j][0]) == int(line[0]):
                if int(dataSchool[j][1]) < int(line[1]):
                    dataSchool.pop(j)
                    dataSchool.append(line)
                    break

dataSchool = sorted(dataSchool, key=lambda k: int(k[0]))
print(" ".join(str(x) for x in [dataSchool[i][1] for i in range(0, len(dataSchool))]))
