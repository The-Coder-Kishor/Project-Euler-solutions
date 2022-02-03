name = open('names.txt', 'r')
s = name.readline()
list = s.split(',')
for i in range(0,len(list)):
    list[i] = list[i].strip('"')
list.sort()
score = []
for i in range(0,len(list)):
    s = 0
    for j in list[i]:
        s = s + (ord(j)-64)
    score.append(s)
final = 0
for i in range(0,len(list)):
    final += (i+1)*score[i]
print(final)