# Created by Yuliya Belyashik
# olympiad
# 2018-11-07


def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}


schoolData = {}

for line in open('input.txt', 'r', encoding='utf8'):
    line = line.replace('\n', '').split(' ')
    if schoolData.get(line[2]) == None:
        addData = {line[2]: int(line[3])}
        schoolData.update(addData)
    else:
        updData = {line[2]: int(schoolData.get(line[2])) + int(line[3])}
        schoolData.update(updData)


sortSchool = list(find_key(schoolData, max(schoolData.values())))

print(" ".join(str(x) for x in sorted(sortSchool)))
