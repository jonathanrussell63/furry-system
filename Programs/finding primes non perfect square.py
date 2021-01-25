import math
import time
b= 4
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while n%i==0: 
        	n=n/i
        i=i+1
      	return 2
    return n
print(largest_prime_factor(b))
# fails on perfect squares

