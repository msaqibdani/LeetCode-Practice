class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key = lambda k : len(k))
        dp = {}
        
        for word in words:
            
            for i in range(len(word)):
                
                prev_word = word[:i] + word[i+1:]
                
                dp[word] = max(dp.get(prev_word, 0)+1, dp.get(word, 0))
        
        return (max(dp.values()))