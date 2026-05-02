class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = [""]
        for digit in digits:
            tmp = []
            for cur in res:
                for c in digit_to_char[digit]:
                    tmp.append(cur + c)
            res = tmp
        return res