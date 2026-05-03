class Solution:
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     adj = defaultdict(list)
    #     for src, dst in sorted(tickets, reverse=True):
    #         adj[src].append(dst)

    #     ans = []
    #     def dfs(src):
    #         while adj[src]:
    #             dst = adj[src].pop()
    #             dfs(dst)
    #         ans.append(src)

    #     dfs("JFK")
    #     return ans[::-1]
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        ans = []
        def dfs(cur):
            while adj[cur]:
                dfs(adj[cur].pop())
            ans.append(cur)

        dfs("JFK")
        return ans[::-1]

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     adj = defaultdict(list)
    #     for src, dst in sorted(tickets, reverse=True):
    #         adj[src].append(dst)

    #     ans = []
    #     st = ["JFK"]

    #     while st:
    #         cur = st[-1]
    #         if not adj[cur]:
    #             ans.append(st.pop())
    #         else:
    #             st.append(adj[cur].pop())

    #     return ans[::-1]