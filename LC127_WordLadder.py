class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        '''
        #preprocess data
        
        hit -> [hia ... hiz] or [hat ... hzt] or [ait ... zit]
        
        '''
        from collections import defaultdict, deque
        
        def preprocess(ls):
            
            mapping = defaultdict(list)
            
            for word in ls:
                for i in range(len(word)):
                    temp = word[:i] + '*' + word[i + 1:]
                    mapping[temp].append(word)
 
            return mapping
        
        if endWord not in wordList: return 0
        mapping = preprocess(wordList)
        
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append((beginWord, 1))
        
        
        while q:
            
            curr_word, level = q.popleft()
            
            if curr_word == endWord:
                return level
            
            
            for i in range(len(curr_word)):
                temp = curr_word[:i] + '*' + curr_word[i + 1:]
                
                if temp not in visited:
                    visited.add(temp)
                    
                    for possible_routes in mapping[temp]:
                        q.append((possible_routes, level + 1))
        
        
        return 0
                
            