class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x_list = []
        y_list = []
        counter = 0
        for i in nums:
            if counter < n:
                x_list.append(i)
                counter+=1
            else:
                y_list.append(i)
        print(x_list)
        print(y_list)
        shuffled_list = []
        for i in range(n):
            shuffled_list.append(x_list[i])
            shuffled_list.append(y_list[i])
        return shuffled_list
    
s = Solution()

print(s.shuffle([1,1,2,2],2))
                
            