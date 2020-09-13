from collections import defaultdict
def removeInvalidParentheses(string):
  
  final_results = defaultdict(set)
  dp = {}
  
  
  #'(())'
  def isValid(string):
    
    stack = []
    
    for letter in string:
      
      #not a ()
      if letter not in ['(', ')']:
        continue
      
      #is ()
      else:
        
        #if it's open paranthesis (
        if letter == '(': stack.append(letter)
        
        #if letter == )
        else:
          if not stack: 
            return False
          
          last_in_stack = stack.pop()
          if last_in_stack != '(': 
            return False
    
    return len(stack) == 0
      
       
  
  def helper(index, current_string, number_removed):
    
    if index == len(string):
      if isValid(current_string):
        final_results[number_removed].add(current_string)
        return True
      
      else:
        return False
    
    
    if (index, number_removed) in dp:
      return dp[(index, number_removed)]
    
    
    for i in range(index, len(string)):
      
      if string[i] not in ['(', ')']:
        helper(i+1, current_string, number_removed)
        continue
      
      #keep one
      condition = helper(i+1, current_string, number_removed)
      
      #remove one
      new_string = current_string[:i] + current_string[i+1:]
      condition_1 = helper(i+1, new_string, number_removed + 1)
      
      if condition:
        dp[(index, number_removed)] = True
      
      if condition_1:
        dp[(index, number_removed + 1)] = True
      
      
  
  
  helper(0, string, 0)
  return final_results