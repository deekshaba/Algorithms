f=open("C:\\Users\\deeksha\\Desktop\\categories.txt")
map={}
set=[]
for row in f.readlines():
    values = row.split(';')
    values[len(values) - 1] = values[len(values) - 1].split('\n')[0]
    for value in values:
        if value in map:
            map[value] += 1
        else:
            map[value] = 1
f.close()
f=open("C:\\Users\\deeksha\\Desktop\\pattern1.txt","w")
for value in map.keys():
    if map[value] > 771:
        f.write("%d:%s\n" %(map[value],value))
        set.append(value)
f.close()

couples = {}
for i in range(0, len(set) - 1):
  for j in range(i+1,len(set)):
       couples['{};{}'.format(set[i],set[j])] = 0
print(len(set))
print(len(couples))


f=open("C:\\Users\\deeksha\\Desktop\\categories.txt")
for row in f.readlines():
    values = row.split(';')
    values[len(values) - 1] = values[len(values) - 1].split('\n')[0]
    for i in range(0,len(values)-1):
        for j in range(i+1,len(values)):
            key1 = '{};{}'.format(values[i],values[j])
            key2 = '{};{}'.format(values[j],values[i])
            if key1 in couples.keys():
                couples[key1] += 1
            if key2 in couples.keys():
                couples[key2] += 1
f.close()

f=open("C:\\Users\\deeksha\\Desktop\\pattern2.txt","w")
for key in couples.keys():
    if couples[key] > 771:
        f.write("%d:%s\n" %(couples[key], key))
f.close()
      

