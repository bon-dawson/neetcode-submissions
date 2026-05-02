class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            degrees[a] += 1
            adj[b].append(a)

        q = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        ans = []
        while q:
            current_subject = q.popleft()
            ans.append(current_subject)

            for next_subject in adj[current_subject]:
                degrees[next_subject] -= 1
                if degrees[next_subject] == 0:
                    q.append(next_subject)

        return ans if len(ans) == numCourses else []