class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
       
        ops = []
        j = 0

        stack = []
        
        print(len(target))
        for i in range(1,n+1):
            stack.append(i)
            ops.append("Push")
            if i == target[j]:
                j+=1
                print(j)
                if j == len(target):
                    return ops
                
            else:
                stack.pop()
                ops.append("Pop")
        return ops

    

    
s = Solution()

print(s.buildArray([1,3],3))
