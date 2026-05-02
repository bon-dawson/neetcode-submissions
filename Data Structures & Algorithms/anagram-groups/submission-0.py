class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            freq = Counter(s)
            key = ""
            for i in range(26):
                key += str(freq[chr(i + 97)]) + "#"
            groups[key].append(s)

        ans = []
        for value in groups.values():
            ans.append(value)
        
        return ans