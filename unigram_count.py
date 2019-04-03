f = open('input.txt','r')
dic = {0:"a"}
count = 0
while True:
	line = f.readline()
	if not line: break
	line=line.split()
	count +=len(line)
	for i in range(len(line)):
		if(dic.get(str(line[i]))==None): 
			dic[str(line[i])] = 1
		else: 
			dic[str(line[i])] = dic[str(line[i])] + 1
del dic[0]
f.close()