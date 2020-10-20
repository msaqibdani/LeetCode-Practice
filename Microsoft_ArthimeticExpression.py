'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer 
and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).


[*, +, 3, 2, +, 4, 5]
[3, +, 2, *, 4, +, 5]

'''
class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None




def evaluate(root):

	operations = {
	'-': lambda x, y: x - y,
	'+': lambda x, y: x + y,
	'/': lambda x, y: x / y,
	'*': lambda x, y: x * y
	}



	def helper(root):

		if type(root.val) == int:
			return root.val


		else:

			left = helper(root.left)
			right = helper(root.right)

			return operations[root.val](left, right)


	return helper(root)


'''
    *
   / \
  +    +
 / \  / \
3  2  4  5

'''

a = Node('*')
b = Node('+')
c = Node('+')
d = Node(3)
e = Node(2)
f = Node(4)
g = Node(5)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

print(evaluate(a))














