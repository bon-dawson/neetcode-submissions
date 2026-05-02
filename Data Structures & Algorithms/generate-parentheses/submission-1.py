class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(cur, cnt, o, c):
            if o == c and o == n:
                res.append(cur)
                return

            if o > n:
                return

            backtracking(cur + "(", cnt + 1, o + 1, c)
            if o > c:
                backtracking(cur + ")", cnt + 1, o, c + 1)

            
        backtracking("", 0, 0, 0)

        return res