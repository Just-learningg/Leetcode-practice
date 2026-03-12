class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        small_than = []
        smaller = 0
        for i in nums:
            for j in nums:
                if i > j:
                    smaller+=1
            small_than.append(smaller)
            smaller = 0