class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l <= r:
            s = numbers[l] + numbers[r]
            m = (l + r) // 2
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r = r - 1
            else:
                l = l + 1
        return []
        