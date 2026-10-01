class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {} # number -> count
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        pair = 0
        for k in count.values():
            pair += k * (k - 1) // 2
        return pair