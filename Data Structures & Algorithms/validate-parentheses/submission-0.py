class Solution:
    def isValid(self, s: str) -> bool:

        # Solution: Using a hashmap and a stack
        mapping = {')':'(', '}': '{', ']':'['}
        stack = [] 

        for c in s: 
            if c in mapping: # if closed bracket is in map 
                if len(stack) != 0 and stack[-1] == mapping[c]: # if stack has existing element + top of stack = current char's (key) val
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False

        #Ex: [()] where stack[-1] is ), and equals mapping[(] --> ): pop 

        


      