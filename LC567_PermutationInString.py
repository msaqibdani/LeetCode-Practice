from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1_freq = Counter(s1)
        
        window = {}
        start = end = 0
        
        #createWindow
        while end < len(s1):
            letter = s2[end]
            
            window[letter] = window.get(letter, 0) + 1
            
            end+=1
        
        if window == s1_freq:
            return True
        
        
        while end < len(s2):
            next_letter = s2[end]
            first_letter = s2[start]
            start+=1
       
            
            #add next letter and remove first letter in the window
            window[next_letter] = window.get(next_letter, 0) + 1
            window[first_letter] -= 1
            
            #if first letter == 0 then delete the occurence from window
            if window[first_letter] == 0: del window[first_letter]
                
            
            if window == s1_freq:
                return True
            
            
            end+=1
        
        return False
            
        
        
            
        
        
        
        