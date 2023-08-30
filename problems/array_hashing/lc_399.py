from typing import List


class Solution:
    """
    @name: 399. Evaluate Division
    @url: https://leetcode.com/problems/evaluate-division/
    @deps: Array, Depth-First Search, Breadth-First Search, Union Find, Graph, Shortest Path
    """

    def __init__(self) -> None:
        self.adjency_list = {}

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        for i in range(len(equations)):
            a, b = equations[i]
            self.adjency_list[a] = self.adjency_list.get(a, []) + [(b, values[i])]
            self.adjency_list[b] = self.adjency_list.get(b, []) + [(a, 1 / values[i])]

        res = []

        for query in queries:
            res.append(self.dfs(query[0], query[1], set()))

        return res

    def dfs(self, a, b, visited):
        if a not in self.adjency_list or b not in self.adjency_list:
            return -1.0

        if a == b:
            return 1.0

        visited.add(a)
        for node, val in self.adjency_list[a]:
            if node not in visited:
                tmp = self.dfs(node, b, visited)
                if tmp != -1.0:
                    return val * tmp
        return -1.0


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    s = Solution()
    print(s.calcEquation(equations, values, queries))
