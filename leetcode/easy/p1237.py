"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        answer = []
        i, j, k = 0, 0, 1000
        for i in range(1, 1000):
            for j in range(k, 0, -1):
                if customfunction.f(i, j) == z:
                    answer.append([i, j])
                    k = j - 1
                    break
        return answer
