class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        best = 0
        target = 1
        for i in range(len(nums)):
            if target==nums[i]:
                current+=1
                if current > best:
                    best = current
            else:
                current = 0
        print(best)


s = Solution()

s.findMaxConsecutiveOnes([1,1,0,0,1])