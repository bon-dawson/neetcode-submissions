class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev, ans = float("-inf"), 0
        n = len(position)
        car = []
        for i in range(n):
            car.append((position[i], speed[i]))
        car.sort()
        for i in range(n - 1, -1, -1):
            t = (target - car[i][0]) / car[i][1]
            if t > prev:
                prev = t
                ans += 1
        return ans