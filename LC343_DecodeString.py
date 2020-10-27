class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
                
        for letter in s:
            if letter == ']':
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                
                stack.pop() # pop [
                digit = int(stack.pop())
                
                stack.append(string*digit)
            
            else:
                
                if letter.isdigit() and stack and stack[-1].isdigit():
                    stack.append(stack.pop() + letter)
                
                else:
                    stack.append(letter)
                
                
                    
                
            
        return ''.join(stack)
        
        
        
                

        
        