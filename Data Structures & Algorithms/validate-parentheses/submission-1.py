class Solution:
    def isValid(self, s: str) -> bool:
        d={'[':']','{':'}','(':')'}
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if stack and d[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    return False    
        if len(stack)==0:
            return True
        else:
            return False    




        