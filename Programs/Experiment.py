class node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class linked_list:
  def __init__(self):
    self.head = node()

  def append(self,data):
    new_node = node(data)
    cur = self.head
    while cur.next !=None:
      cur = cur.next
    cur.next=new_node

  def len(self):
    cur = self.head
    total = 0
    while cur.next != None:
      total +=1
      cur= cur.next
    return total

  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next != None:
      cur_node = cur_node.next
      elems.append(cur_node.data)

    print(elems)

  def get(self, index):
    if index>=self.len():
      print("ERROR: Index out of range")
      return None
    cur_idx= 0
    cur_node = self.head
    while cur_node !=None:
      cur_node = cur_node.next
      if cur_idx == index:
        return cur_node.data
      cur_idx +=1
    
  def erase(self,index):
    if index>= self.len():
      print('Index not in range')
      return None

    cur_idx = 0 
    cur_node = self.head
    while cur_node !=None:
      last_node =cur_node
      cur_node = cur_node.next
      if cur_idx ==index:
        last_node.next = cur_node.next

      cur_idx+=1




        

def rankIndex(values, rank):
    score_sums = []
    for i in range(len(values)):
        score_sums.append( sum(values[i]))
    sorted_sums = mergeSort(score_sums)
    x = sorted_sums[rank-1]
    indexRank = sorted_sums.index(x)
    return indexRank

# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  

import random
nums = {'0':0, '1':0}
for i in range(0,1000000):
  a = round(random.random())
  if a==0:

    nums['0']+=1
  else:
    nums['1']+=1

print(nums)
