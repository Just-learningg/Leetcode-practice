class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        items = str(x)
        all_items = list(items)
        end = round(len(all_items)/2)
        for i in range(0,end):
            if(all_items[i]!=all_items[-(i+1)]):
                return False
           
        return True




s = Solution()
print(s.isPalindrome(101))

char1 = 'A'
char2 = 'A' 

# if char1==char2:
#     print("yes")
# else:
#     print("no")