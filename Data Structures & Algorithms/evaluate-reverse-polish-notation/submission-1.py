class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == '*':
                st.append(st.pop() * st.pop())
            elif c == '+':
                st.append(st.pop() + st.pop())
            elif c == '-':
                se, fi = st.pop(), st.pop()
                st.append(fi - se)
            elif c == '/':
                se, fi = st.pop(), st.pop()
                st.append(fi / se)
            else:
                st.append(int(c))
        return st[-1]