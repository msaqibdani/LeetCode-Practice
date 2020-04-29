def search(nums, target):

	if not nums:
		return -1


	#find pivot function
	def pivotSearch(arr):

		#initialize pointers l = 0 and len(arr) - 1
		l, r = 0, len(arr) - 1

		while l+1 < r:
			#curr_mid_point
			mid = (l+r)//2

			#if pivot is to the right 
			if arr[mid] > arr[0]:
				l = mid

			#if pivot is to the left
			else:
				r = mid

		#if this is arr[l] is your pivot
		#it is neccessary to check the arr[l] first
		#because numbers are in ascending order and if 
		#arr[l] and arr[r], both, smaller than arr[0]
		#then pivot is always arr[l]
		if arr[l] < arr[0]:
			return l

		#if arr[r] is your pivot
		else:
			return r

	pivot_index = pivotSearch(arr)

	#binary Search to search in either of the sections (before_pivot_section, after_pivot_section)
	def binarySearch(arr, l, r):

		while l+1 < r:

			mid = (l+r)//2
			if arr[mid] == target:
				return mid

			elif arr[mid] > target:
				r = mid

			else:
				l = mid

		if arr[l] == target:
			return l

		elif arr[r] == target:
			return r

		return -1


	#if target is in after_pivot_section
	if target >= nums[pivot_index] and target <= nums[len(arr)-1]:
		return binarySearch(arr, pivot_index, len(nums)-1)

	#if target is in before_pivot_section
	else:
		return binarySearch(arr, 0, pivot_index-1)




arr, target = [4, 5, 6, 7, 0, 1, 2], 0
print('array =', arr, '||', 'target =', target, '||', 'target index = ', search(arr, target))

arr, target = [4, 5, 6, 7, 0, 1, 2], 5
print('array =', arr, '||', 'target =', target, '||', 'target index = ', search(arr, target))

arr, target = [0, 1, 2], 0
print('array =', arr, '||', 'target =', target, '||', 'target index = ', search(arr, target))

arr, target = [1, 2], 0
print('array =', arr, '||', 'target =', target, '||', 'target index = ', search(arr, target))


if __name__ == "main":
	main()
