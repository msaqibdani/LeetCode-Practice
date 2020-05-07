'''
Given an arbitrary ransom note string and another string containing 
letters from all the magazines, write a function that will return true 
if the ransom note can be constructed from the magazines ; otherwise, 
it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''



from collections import Counter
def canConstruct(ransomNote, magazine):

	mag_count = Counter(magazine)
	ran_count = Counter(ransomNote)


	for key, value in ran_count.items():
	    
	    if key not in mag_count:
	        return False
	    
	    elif value > mag_count[key]:
	        return False

	return True