import random
ints = []

for i in range(500):
	ints.append(i)
average=0
for i in range(100):
	found = []
	count=0
	while len(found)<len(ints):
		rand = int(len(ints)*random.uniform(0,1))
		if rand not in found:
			found.append(rand)
		count+=1
	average+=count
print(average/100)

