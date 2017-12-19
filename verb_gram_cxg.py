from pymystem3 import Mystem
# import re
m = Mystem()

f = open('verbs.txt', 'r')
f2 = open('verbs_morph.txt', 'w')
morphs = []
lines = f.readlines()
for line in lines:
	words = line.split(' ')
	for word in words:
		if word.lower().startswith('удар'):
			word = word.strip('\r\n.!?,)(')
			ana = m.analyze(word)
			morphs.append(ana[0]['analysis'][0]['gr'])
print(len(lines) - len(morphs))
f2.write('\n'.join(morphs))
f2.close()
f.close()