from random import random
total_sum=0
dictionary = {}
for i in range (15):
	key = 2**i

	dictionary[str(key)]=0
for i in range(100000000):
	current_sum=0
	rand=random()
	count=0
	while rand<.5:
		current_sum=2**count


		count+=1
		rand=random()
	
	total_sum+=current_sum


print(total_sum/100000000)
