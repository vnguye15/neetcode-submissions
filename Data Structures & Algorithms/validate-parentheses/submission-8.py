class Solution:
    def isValid(self, s: str) -> bool:
        
        # understand
        # input: s (string)
        # output: True/False (boolean)

        # constraints: 
        # brackets must be closed in correct order
        # every bracket has a pair of each other 

        # Examples
        # s = [] --> true
        # s = ([{}]) --> true 

        # Approach - Stack operation 

        # Plan
        # (Edge case): check if string s length is odd --> odd means we have incomplete pair of bracket

        # create a dict: closed bracket (key) : open bracket (val)
        # create a stack 
        # iterate through string s 
        # if a open bracket is found
        #    add it to stack 
        # else 
        #  if top of the stack's bracket matches a closed bracket in data structure (dict)
        #   pop item from stack 
        #   else top of stack bracket does NOT match a closed bracket in data structure (dict): 
        #        return false 
        
        # after popping element, check if len string s is 0 --> return True 

        seen = {')':'(', ']':'[', '}':'{',}
        stack = [] 

        # checking if string s lenght is odd
        if len(s) % 2 != 0:
            return False

        for c in s: 
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:

                #Edge case: string s = ]] --> stack is always empty
                if len(stack) == 0:
                    return False
                if stack[-1] == seen[c]: # if top of stack matches current closed brackets value (open bracket)
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
   

