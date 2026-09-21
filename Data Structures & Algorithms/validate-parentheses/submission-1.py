class Solution:
    def isValid(self, s: str) -> bool:
        
        # Solution to attempt #3 (solution 3)

        stack = []
        seen = {
            ')':'(',
            ']':'[',
            '}':'{', 
        }

        for c in s:
            if c == '(' or c == '[' or c == '{': # current bracket is a open bracket in string s 
                stack.append(c)
            else: 
                # current bracket is a closed bracket in string s 

                if len(stack) == 0: # Example: stack = [], c = ")" 
                    return False

                if stack[-1] == seen[c]: # if stack[ '(' ] == seen[')] which returns '(':
                    stack.pop()
                else:
                    return False # Example: s= "[(])"
                
        if len(stack) == 0:
            return True
        return False


                