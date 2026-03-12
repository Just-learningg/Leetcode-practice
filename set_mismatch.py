class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # counter = nums[0]
        # for i in nums:
        #     if(i==counter):
        #         pass
        #         counter+=1
        #     else:
        #         return i,counter
        # counter = 1
        # match__found = 0
        # for i  in range(len(nums)):
        #     if nums[i] == counter:
        #         counter+=1
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             match__found+=1
        #             if match__found == 2:
        #                 return nums[i], counter
            # if i+1 < len(nums) and nums[i] == nums[i+1]:
            #     return nums[i],counter
        # counter = 1
        # match_found = 0
        # for i in range(len(nums)):
        #     if counter in nums:
        #         counter+=1
        #     else:
        #         for i in nums:
        #             for j in range(len(nums)):
        #                 if i == nums[j]:
        #                     match_found+=1
        #                     if match_found == 2:
        #                         return i,counter
        #             match_found = 0

        # n = len(nums)
        # seen = []

        # duplicate = -1
        # for i in nums:
        #     if i in seen:
        #         duplicate = i
        #     else:
        #         seen.append(i)
        

        # missing = -1
        # for i in range(1,n+1):
        #     print(i)
        #     if i not in nums:
        #         missing = i
        #         break
        #     else:
        #         missing = n+1
        # return [duplicate, missing]
    
        n=len(nums)
        print(n)
        expected_sum=n*(n+1)/2
        print(expected_sum)
        actual_sum=sum(nums)
        print(actual_sum)
        actual_set_sum=sum (set(nums))
        print(actual_set_sum)
        duplicate=actual_sum-actual_set_sum
        missing=expected_sum-actual_set_sum
        return (duplicate,missing)
            


                
                
s = Solution()
print(s.findErrorNums([1,2,2,4]))
#[1,5,3,2,2,7,6,4,8,9]