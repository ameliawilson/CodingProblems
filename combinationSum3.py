########################################################################
# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and 
# each combination should be a unique set of numbers.
#
# Example: Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#
# [Problem 216]
########################################################################

from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # all combinations of k elements from 1-9, no repeats
        c = combinations(range(1,10), k)
        sol = []
        
        for i in c:
            if sum(i) == n:
                sol.append(list(i))
        
        return sol
