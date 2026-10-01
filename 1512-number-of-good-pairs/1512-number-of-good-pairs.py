class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {} # number -> count
        res = 0
        for x in nums:
            res += count.get(x, 0)
            count[x] = 1 + count.get(x, 0)
        return res