class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=='+':
                a=stack[-1]
                b=stack[-2]
                stack.pop()
                stack.pop()
                c=a+b
                stack.append(c)
            elif tokens[i]=='-':
                a=stack[-1]
                b=stack[-2]
                stack.pop()
                stack.pop()
                c=b-a
                stack.append(c)
            elif tokens[i]=='*':
                a=stack[-1]
                b=stack[-2]
                stack.pop()
                stack.pop()
                c=a*b
                stack.append(c)
            elif tokens[i]=='/':
                a=stack[-1]
                b=stack[-2] 
                stack.pop()
                stack.pop()
                c=b/a
                stack.append(int(c))
            else:
                stack.append(int(tokens[i]))
        return (stack[0])            
