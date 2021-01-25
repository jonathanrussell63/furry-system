# lightweight verison of a hash table. Efficient insertions and lookups
# more space efficient than hash table, but tis comes at the cost of haing 'false positives' for entry lookup
# when to use: when you want a data structure for fast lookups and insertions as well as space use. I don't care if the data structure sometimes tells me
# if something is there when it isn't
# i.e. I don't care if a blocked ip address is occasionally able to access a blocked site since storing massive number of ip addresses is bad for space

#pokedex BloomFilter
# bit vector = a list of bits 
bit_vector = [0]*20
#non-cryptographic hash function (Murmur and FNV) to turn on bits after we find one
# for some reason i can't pip install pyhash
import pyhash
# these calculate the output of FNV and Murmur
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()
fnv_pika = fnv('Pikachu') % 20
fnv_char = fnv('Charmander') % 20

murmur_pika = murmur('Pikachu') % 20
murmur_char = murmur('Charmander') % 20

bit_vector[fnv_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_pika]=1
bit_vector[murmur_char]=1


# A wild Bulbasaur appear!
fnv_bulb = fnv('Bulbasaur') % 20
murmur_bulb = murmur('Bulbasaur') % 20

if bit_vector[fnv_bulb]!=1 and bit_vector[murmur_bulb]!=1:
	print('Not yet in pokedex')