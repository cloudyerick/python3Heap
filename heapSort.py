

#O[nlg(n)]
def MaxHeapSort(list):
	#O(n) - half for more of the nodes will be leafs
	def buildHeap(list):
		start = int((len(list) - 2) / 2)
		while start >= 0:
			shiftDown(list, start, len(list) - 1)
			start -= 1
	#O[lg(n)]
	def shiftDown(list, index, end):
		root = index
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if child + 1 <= end:
				if list[child] < list[child + 1]:
					child += 1
			if list[root] < list[child]:
				list[child], list[root] = list[root], list[child] 
				root = child
			else:
				return

	buildHeap(list)



#O[nlg(n)]
def MinHeapSort(list):
	#O(n) - half for more of the nodes will be leafs
	def buildHeap(list):
		start = int((len(list) - 2) / 2)
		while start >= 0:
			shiftDown(list, start, len(list) - 1)
			start -= 1
	#O[lg(n)]
	def shiftDown(list, index, end):
		root = index
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if child + 1 <= end:
				if list[child] > list[child + 1]:
					child += 1
			if list[root] > list[child]:
				list[child], list[root] = list[root], list[child] 
				root = child
			else:
				return

	buildHeap(list)


list = [31,	70,	70,	30,	78, 97,	16,	55,	8, 76]

list2 = [33, 45]

list3 = [33, 45, 29]

list4 = [1, 12, 15, 0]

list5 = [31,70,	70,	30,	78, 97,	16,	55,	8, 76, 20 , 1, 100]


MaxHeapSort(list)
MaxHeapSort(list2)
MaxHeapSort(list3)
MaxHeapSort(list4)
MaxHeapSort(list5)

print (list)
print (list2)
print (list3)
print (list4)
print (list5)

MinHeapSort(list)
MinHeapSort(list2)
MinHeapSort(list3)
MinHeapSort(list4)
MinHeapSort(list5)

print (list)
print (list2)
print (list3)
print (list4)
print (list5)






