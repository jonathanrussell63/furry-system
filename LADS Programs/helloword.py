import math

u1 = []
u2 = []

for i in range(122):
	if math.gcd(122,i)==1:
		u1.append(i)

for i in range(124):
	if math.gcd(124,i)==1:
		u2.append(i)

dic1= {}
dic2= {}
for i in range(1,61):
	dic1[i] = 0
	dic2[i] = 0

for j in range(60):
	count = 1
	t = True
	while t:
		if (u1[j]**count)%122==1:
			dic2[count]+=1
			#print(u1[j], '   ', count)
			count =1

			t = False
			
		count+=1
#print(u1)
#print()
for j in range(60):
	count = 1
	t = True
	while t:
		if (u2[j]**count)%124==1:
			dic2[count]+=1
			#print(u2[j], '   ', count)
			count =1

			t = False
			
		count+=1
#print(u2)

sss1 = []
for i in range(60):
	for j in range(1,61):
		if (u1[i]**j)%(122)==1:
			sss1.append(j)
			break

sss2 = []
for i in range(60):
	for j in range(1,61):
		if (u2[i]**j)%(124)==1:
			sss2.append(j)
			break

print(sss1)

dict1 = {}
for i in range(1,61):
	dict1[i] = 0

for k in range(60):
	dict1[sss1[k]] +=1

dict2 = {}
for i in range(1,61):
	dict2[i] = 0

for k in range(60):
	dict2[sss2[k]] +=1

print(dict1)
print()
print(dict2)