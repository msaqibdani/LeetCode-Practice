class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.trie
        
        for letter in word:
            temp = self.addLetter(temp, letter)
        
        temp['.'] = word
        
            
    
    def addLetter(self, trie_map, letter):
        
        if letter not in trie_map:
            trie_map[letter] = {}
        
        return trie_map[letter]
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        found = self.search_prefix(word)
        
        if found != False:
            return True if '.' in found else False
        
        return False
        
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.search_prefix(prefix)
        
        if temp:
            return True
        
        return False
        
    
    def search_prefix(self, word):
        index = 0
        temp = self.trie
        
        while index < len(word):
            
            letter = word[index]
            
            if letter not in temp:
                return False
            
            temp = temp[letter]
            index+=1
        
        return temp
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)