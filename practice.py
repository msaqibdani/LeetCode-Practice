from collections import deque
class MaxQueue():
	def __init__(self):
		q = deque()
		max_q = deque()

	def push(num):
		if not q:
			max_q.append(num)
			q.append(num)

		else:
			while max_q[0] <= num:
				max_q.popleft()


		

	def pop():
		

	def max_num():
		return


'''

[9, 5, 7, 1]

[9, 5, 7, 1]


-> how to track the max. If I have two q's how would that help me? 

'''








def BFS(graph):
	
	#initialize a queue
	q = queue()
	visited = set()

	q.add(start)
	visited.add(start)

	#while loop  - till queue is not empty
	while q:

		#remove the element from the start of the queue
		curr_element = q.popleft()

		#doSomething
		if curr_element == 'answer':
			return curr_element

		#get all the neighbors 
		neighbors = getNeighbors(graph, curr_element)

		#add all neighbors to queue
		for nei in neighbors:

			if nei not in visited:
				q.append(nei)
				visited.add(nei)



def numberOfIslands(grid, start = (0, 0)):

	visited = set()
	count  = 0

	for r in range(len(grid)):
		for c in range(len(grid[0])):

			if grid[r][c] == '1':
				count += 1
				dfs(r, c, grid, visited)


def dfs(r, c, grid, visited):

	visited.add((r, c))
	stack = [(r, c)]

	while stack:

		curr_r, curr_c = stack.pop()

		neighbors = getNeighbors(grid, curr_r, curr_c)

		for nei_r, nei_c in neighbors:

			if (nei_r, nei_c) not in visited and grid[nei_r][nei_c] == '1':
				stack.append((nei_r, nei_c))
				visited.add((nei_r, nei_c))






def dfsTraversal(graph, node):

	visited = set()

	def dfs_1(graph, curr_element):

		#do something
		if curr_element == 'answer':
			return curr_element

		neighbors = getNeighbors(graph, curr_element)

		for nei in neighbors:

			if nei not in visited:
				visited.add(nei)
				dfs(graph, nei)




