class MinStack:

    def __init__(self):
        self.st = []
        self.mn_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.mn_st:
            val = min(val, self.mn_st[-1])
        self.mn_st.append(val)
        
    def pop(self) -> None:
        self.st.pop()
        self.mn_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn_st[-1]