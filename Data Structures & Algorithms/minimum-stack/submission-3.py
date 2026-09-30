class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        
        self.s.append(val)

        if not self.m:
            self.m.append(val)
            return

        if  val <= self.m[-1]  :
            self.m.append(val)
            return 
        

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.m[-1]:
            self.m.pop()
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1] 
