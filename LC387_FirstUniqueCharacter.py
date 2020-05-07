'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.


Note: You may assume the string contain only lowercase letters.
'''

from collections import OrderedDict
def firstUniqChar(self, s: str) -> int:

	order = OrderedDict()

	for index, letter in enumerate(s):
	    if letter in order:
	        order[letter].append(index)
	    else:
	        order[letter] = []
	        order[letter].append(index)


	for key, value in order.items():
	    if len(value) == 1:
	        return value[0]

	return -1
            
        
