'''
Overall Time Complexity of the count sort is O(len(arr) + len(count_arr))
Generally use when the arr[i] has an upperbound 

'''
arr = 'fabdcde'
def countingSort(arr):

	#count = [0] * (max(arr) + 1)
	count = [0] * 26

	for ele in arr:
		count[ord(ele) - 97] += 1

	print(count)

	final_arr = [0] * len(arr)
	j = 0

	for i in range(len(count)):
		freq, k  = count[i], 0
		
		while k < freq:
			final_arr[j] = chr(i + 97) 
			k += 1
			j += 1


	print(final_arr)

countingSort(arr)