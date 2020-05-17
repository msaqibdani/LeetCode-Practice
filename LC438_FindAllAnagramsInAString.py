from collections import Counter
def findAnagrams(self, s: str, p: str) -> List[int]:
    
    if len(s) < len(p):
        return []
    
    start = end = 0
    window = {}
    p_counter = Counter(p)
    ans = []
    
    #create window
    while end < len(p):
        
        letter = s[end]
        window[letter] = window.get(letter, 0) + 1
        end+=1
    
    if window == p_counter: ans.append(0)
        
    while end < len(s):
        next_letter = s[end]
        first_letter = s[start]
        start+=1
        
        
        #add next letter and remove first letter in the window
        window[next_letter] = window.get(next_letter, 0) + 1
        window[first_letter] -= 1
        
        #if first letter == 0 then delete the occurence from window
        if window[first_letter] == 0: del window[first_letter]
        
        if window == p_counter:
            ans.append(start)
        
        
        end+=1
    
    return ans