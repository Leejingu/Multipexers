import operator


f = open('input.txt','r')
unigram = {0 : "a"}
bigram = {0 : "a"}
trigram = {0 : "a"}
count = 0

while True:
	line = f.readline()
	if not line: break
	line=line.split()

### make unigram list	
	for i in range(len(line) - 1):
		if(bigram.get(str(line[i] + " "  + line[i+1])) == None): 
			bigram[str(line[i] + " "  + line[i+1])] = 0

#### ALL trigram count for
	for i in range(len(line) - 2):
		#print(str(line[i] + " " + line[i+1]))
		if(bigram.get( str(line[i] + " " + line[i+1]) ) != None) and i < len(line)-2:
			bigram[str(line[i]+" "+line[i+1])]+=1

#### make trigram list
	for i in range(len(line)-2):
		if trigram.get(str(line[i]+" "+line[i+1]+ " " + line[i+2])) == None:
			trigram[str(line[i]+ " " + line[i+1] + " " + line[i+2])] = 1
		else:
			trigram[str(line[i]+ " " + line[i+1] + " " +line[i+2])] +=  1 

del unigram[0]
del bigram[0]
del trigram[0]

#print(bigram)
f.close()
#print(unigram)
#print(bigram)
probability = {0:0}

for i in trigram.keys():
	probability[i] = trigram[i]/bigram[str(i.split()[0]+" "+i.split()[1])]
del probability[0]

for i in trigram.keys():
	print(i, " = ", probability[i])

f = open('input.txt','r')
line = f.readline()
line_list = line.split()
k = 1
for i in range(len(line_list)-2):
	k*=(probability[line_list[i]+" "+line_list[i+1]+" "+line_list[i+2]])
print(line," = ",k)
f.close()


from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open('input.txt','r').read()
wordcloud = WordCloud(font_path = 'AppleGothic.ttf', 
							relative_scaling = 0.2,
							background_color = 'white').generate_from_frequencies(trigram)
plt.figure(figsize = (12,12))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()