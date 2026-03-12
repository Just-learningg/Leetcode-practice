class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        print(n)
        expected_value = n*(n+1)/2
        actual_value_set = sum(set(nums))
        actual_value = sum(nums)
        print(expected_value)
        print(actual_value)

        diff = expected_value-actual_value_set
        diff_2 = actual_value-actual_value_set
        print(diff)
        print(diff_2,diff-diff_2)
        
    

s = Solution()

s.findDisappearedNumbers([5,3,2,7,2,3,1])

#[4,3,2,7,8,2,3,1] --> 5,6 
#[4,3,2,7,2,3,1] --> 5,6 
#[5,3,2,7,2,3,1] --> 