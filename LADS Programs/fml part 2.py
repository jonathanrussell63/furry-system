import math
u1 = []
u2 = []

for i in range(122):
	if math.gcd(122,i)==1:
		u1.append(i)

for i in range(124):
	if math.gcd(124,i)==1:
		u2.append(i)

print(u1)
print()
print(u2)