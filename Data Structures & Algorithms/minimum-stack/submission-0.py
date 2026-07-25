class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        m=float('inf')
        for i in range(len(self.stack)):
            m=min(m,self.stack[i])
        return m    

        
        
