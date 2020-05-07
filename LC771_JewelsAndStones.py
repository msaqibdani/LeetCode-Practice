'''
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0

'''

from collections import Counter
def numJewelsInStones(J, S):
    #freq counter for J
    count_J = Counter(J)

    #freq counter for S
    count_S = Counter(S)

    #total jewels
    total = 0

    for jewel in count_J.keys():
        
        #if jewel found in S, add the count to total.
        #otherwise add 0
        total += count_S.get(jewel, 0)

    return total